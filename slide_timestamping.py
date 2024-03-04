import numpy as np
import cv2
import json

import os

from SliTraNet.data.data_utils import *
from face_detection import FaceDetector
from slide_similarity import ImageComparator, SlideComparator
import SliTraNet.slide_detection_2d as SliTraNet

# Calculate the x coordinates that have been cropped to not include x1 and x2
def get_cropped_x_coords(x0, x1, frame_x0=0, frame_x1=852):
    x0_difference = abs(x0 - frame_x0)
    x1_difference = abs(x1 - frame_x1)
    
    padding = 50
    if x0_difference < x1_difference:
        return x1 + padding, frame_x1
    else:
        return frame_x0, x0 - padding

# Calulate the bounding box that excludes the face overlay
def get_bounding_box(video_path):
    cap = cv2.VideoCapture(video_path)
    face_detector = FaceDetector()
    bounding_boxes = face_detector.detect_face(video_path)
    
    if len(bounding_boxes) == 0:
        bounding_box = [0, 0, cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)]
    else:
        # Only interested in the x coordinates of the bounding box (delete second and last column)
        x_coords = np.delete(bounding_boxes, np.s_[1::2], axis=1)
        m_x, m_w = np.median(x_coords, axis=0)
        
        x0, x1 = get_cropped_x_coords(m_x, m_x + m_w, frame_x1=cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        bounding_box = [x0, 0, x1, cap.get(cv2.CAP_PROP_FRAME_HEIGHT)]
    
    return np.array([round(x) for x in bounding_box])

def get_frame(video_capture, frame_id):
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    success, frame = video_capture.read()
    
    if not success:
        raise Exception("Could not read from video")
    
    return frame

def save_frame(frame, dir, file_name):
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    cv2.imwrite(dir + file_name, frame)

# Identifies the timestamp of each slide, taken from a video
def get_slide_timestamps(video_path, slides_json, output_folder):
    # Get bounding box of the video with the face overlay cropped out
    bounding_box = get_bounding_box(video_path)

    # Attempt to find the initial slide transitions using the neural network
    try:
        slide_transitions = SliTraNet.test_resnet2d(video_path, bounding_box)
    except:
        return False, None
    
    # Find the fps of the video
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Crop each frame and save the cropped frame as an image, storing the path
    slide_transitions.pop(-1, None)
    frame_paths = []
    for slide_no, (start, end) in slide_transitions.items():
        frame = crop_frame(get_frame(cap, start), *bounding_box)
        dir = output_folder + "frames/"
        file_name = f"cropped_frame{slide_no}.png"
        save_frame(frame, dir, file_name)
        frame_paths.append(dir + file_name)
    print(slide_transitions)
    print(frame_paths)

    # combined_timestamps = combine_timestamps(slide_transitions, frame_paths, slides_json)
    timestamps = match_frames(slide_transitions, frame_paths, slides_json)
    
    return True, timestamps

def merge_timestamps(curr_frame, curr_slide, timestamps):
    (_, end_curr) = curr_frame
    start = timestamps[curr_slide][-1]["start"]
    timestamps[curr_slide][-1] = {"start" : start, "end": end_curr}
    
    return timestamps

def match_frames(slide_transitions, frames, slides_info):
    comparator = SlideComparator()
        
    slides = list(filter(lambda slide: not bool(slide.get("squashed")), slides_info["slides"]))
    num_slides = len(slides)
    
    currentSlide = 0
    num_timestamps = 0

    def compareTillMatch(frameNo, slideNo, gap=1):
        can_go_forward = slideNo + gap < num_slides
        can_go_back = slideNo - gap >= 0
        
        if can_go_forward:
            is_similar = comparator.is_similar(frames[i], slides[slideNo + gap], False)
            if is_similar:
                return slideNo + gap

        if can_go_back:
            is_similar = comparator.is_similar(frames[i], slides[slideNo - gap], False)
            if is_similar:
                return slideNo - gap

        if not can_go_back and not can_go_forward:
            return -1
        else:
            return compareTillMatch(frameNo, slideNo, gap + 1)

    timestamps = {}
    for i in range(len(frames)):
        is_similar = comparator.is_similar(frames[i], slides[currentSlide], False)
        should_merge = True
        if not is_similar:
            match = compareTillMatch(i, currentSlide)

            if (match != -1):
                should_merge = False
                currentSlide = match

        if (currentSlide not in timestamps):
            timestamps[currentSlide] = []
            
        if should_merge and len(timestamps[currentSlide]) != 0:
            timestamps = merge_timestamps(slide_transitions[i], currentSlide, timestamps)
        else: 
            start, end = slide_transitions[i]
            timestamps[currentSlide].append({"start": int(start), "end": int(end)})
        
    return timestamps

if __name__ == "__main__":
    slides_json = """{
        "num_slides": 7,
        "slides": [
            "Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-01.png",
            "Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-02.png",
            "Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-03.png",
            "Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-04.png",
            "Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-05.png",
            "Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-06.png",
            "Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-07.png"
        ]
    }
    """
    result, slide_timestamps = get_slide_timestamps("video.mp4", slides_json)
    if result:
        print(slide_timestamps)
    else:
        print("Fetching slide timestamps failed")
