# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 18:16:03 2021

Code is partly based on https://git.aweirdimagination.net/perelman/slide-detector

@author: Aline Sindel
"""

import random

import numpy as np
import cv2

import torch
import torch.nn as nn

import decord
from decord import VideoReader

from .model import *

from .data.data_utils import *
from .data.video_clip_dataset import BasicTransform


def detect_initial_slide_transition_candidates_resnet2d(net, videofile, base, roi, load_size_roi, patch_size, 
                                                        in_gray=True, slide_thresh=8, video_thresh=13):
    # load video file
    vr = VideoReader(videofile, width=load_size_roi[1], height=load_size_roi[0]) 
    
    #determine number of frames
    N_frames = len(vr)  
    anchor_frame = None
    anchor_frame_idx = -1
    video_frame_idx = None
    prev_video_frame_idx = None
    slide_id = -1
    slide_ids = []
    frame_ids_1 = []
    frame_ids_2 = []
    
    if in_gray:
        data_shape = "2_channel"
        input_nc = 2
    else:
        data_shape = "6_channel"
        input_nc = 6
    my_transform = BasicTransform(data_shape = data_shape) #, blur = opt.blur)
    activation = nn.Sigmoid()
    
    for i in range(N_frames):

        frame = vr[i]
 
        imgs = torch.zeros((2,patch_size,patch_size,int(input_nc/2)))
            
        if in_gray: #opencv rgb2gray for torch
            frame = 0.299*frame[...,0]+0.587*frame[...,1]+0.114*frame[...,2]
            frame = frame.unsqueeze(2)
        
        # crop to bounding box region
        frame = crop_frame(frame,roi[0],roi[1],roi[2],roi[3]) 
        #scale to max size (in case patch size changed)
        img_max_size = max(frame.shape[0], frame.shape[1])
        scaling_factor = patch_size / img_max_size
        if scaling_factor != 1:            
            frame = cv2.resize(frame, (round(frame.shape[1] * scaling_factor), round(frame.shape[0] * scaling_factor)), interpolation = cv2.INTER_NEAREST)
            H,W,C = frame.shape
            imgs[1,:H,:W,:C] = frame
        else:
            H,W,C = frame.shape
            imgs[1,:H,:W,:C] = frame
        
        #set anchor
        if anchor_frame == None:
            imgs[0,:H,:W,:C] = frame
            anchor_frame_idx = i 
            anchor_frame = frame
        else:
            imgs[0,:H,:W,:C] = anchor_frame
            
        imgs = my_transform(imgs)
        
        with torch.no_grad():
            # imgs = imgs.cuda()
             
            pred = net(imgs.unsqueeze(0))
            pred = pred.squeeze(1)            
            pred = activation(pred)
            #print(pred)
            if pred<0.5: #transition (class 0)
                if (i - anchor_frame_idx) > slide_thresh: #static frame
                    if video_frame_idx is not None: 
                        if (video_frame_idx - prev_video_frame_idx) > video_thresh:
                            print("video frame {} at {} to {}".format(-1,prev_video_frame_idx+1, video_frame_idx+1))
                            slide_ids.append(-1)
                            frame_ids_1.append(prev_video_frame_idx+1)
                            frame_ids_2.append(video_frame_idx+1) 
                        video_frame_idx = None
                        prev_video_frame_idx = None
                    
                    slide_id += 1
                    print("static slide {} at {} to {}".format(slide_id,anchor_frame_idx+1, i))
                    slide_ids.append(slide_id)
                    frame_ids_1.append(anchor_frame_idx+1)
                    frame_ids_2.append(i)

                else:
                   #video frame or grad transition
                   video_frame_idx = anchor_frame_idx
                   if prev_video_frame_idx is None:
                       prev_video_frame_idx = anchor_frame_idx                  
                #update anchor
                anchor_frame_idx = i
                anchor_frame = frame 
               
    print(len(frame_ids_1)) 
    frame_ids_1 = np.array(frame_ids_1)
    frame_ids_2 = np.array(frame_ids_2)

    transitions = {}
    for slide_id,frame_id_1,frame_id_2 in zip(slide_ids,frame_ids_1,frame_ids_2):               
        transitions[slide_id] = (frame_id_1, frame_id_2)
    
    return transitions
            
def test_resnet2d(video_path, bounding_box, weights_path="Frame_similarity_ResNet18_gray.pth", 
                  patch_size=256):
    torch.manual_seed(0)
    random.seed(0)
    
    ####### Create model
    # --------------------------------------------------------------- 
    net = define_resnet2d()  
    # net = net.cuda()
    net = loadNetwork(net, weights_path, checkpoint=False, prefix='')
    net.eval()

    #### Create dataloader
    # ---------------------------------------------------------------    
    if not is_video_file(video_path):
        raise Exception("File is an unsupported type of video")

    decord.bridge.set_bridge('torch')
    
    print("Processing video {}".format(video_path))
    
    base, roi, load_size_roi = determine_load_size_roi(video_path, bounding_box, patch_size)
        
    return detect_initial_slide_transition_candidates_resnet2d(net, video_path, base, roi, load_size_roi, patch_size)
                  
# if __name__ == '__main__':
    # parser = argparse.ArgumentParser('slide_detection') 
    # parser.add_argument('--dataset_dir', help='path to dataset dir',type=str, default='C:/Users/Sindel/Project/Data/datasets/LectureVideos') 
    # parser.add_argument('--out_dir', help='path to dataset dir',type=str, default='C:/Users/Sindel/Project/Code/SliTraNet/results/test/resnet18_gray')
    # parser.add_argument('--backbone_2D', help='name of backbone (resnet18 or resnet50)',type=str, default='resnet18')   
    # parser.add_argument('--model_path', help='path of weights',type=str, default='C:/Users/Sindel/Project/Code/SliTraNet/weights/Frame_similarity_ResNet18_gray.pth')
    # parser.add_argument('--load_checkpoint', type=bool, default=False, help='model_path is path to checkpoint (True) or path to state dict (False)')
    # parser.add_argument('--slide_thresh', type=int, default=8, help='threshold for minimum static slide length')
    # parser.add_argument('--video_thresh', type=int, default=13, help='threshold for minimum video length to distinguish from gradual transition')
    # parser.add_argument('--patch_size', type=int, default=256, help='network input patch size')
    # parser.add_argument('--n_class', type=int, default=1, help='number of classes')
    # parser.add_argument('--input_nc', type=int, default=2, help='number of input channels for ResNet: gray:2, RGB:6')
    # parser.add_argument('--in_gray', type=bool, default=True, help='run network with grayscale input, else RGB')
    # parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')


    # opt = parser.parse_args()  

    # test_resnet2d()