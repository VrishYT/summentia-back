import numpy as np
import cv2
import json

from os import listdir
from os.path import isfile, join

from SliTraNet.data.data_utils import *
from face_detection import FaceDetector
from slide_similarity import ImageComparator
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
    face_detector = FaceDetector()
    bounding_boxes = face_detector.detect_face(video_path)
    
    # Only interested in the x coordinates of the bounding box (delete second and last column)
    x_coords = np.delete(bounding_boxes, np.s_[1::2], axis=1)
    m_x, m_w = np.median(x_coords, axis=0)
    
    cap = cv2.VideoCapture(video_path)
    x0, x1 = get_cropped_x_coords(m_x, m_x + m_w, frame_x1=cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    bounding_box = [x0, 0, x1, cap.get(cv2.CAP_PROP_FRAME_HEIGHT)]
    return np.array([round(x) for x in bounding_box])

def get_frame(video_capture, frame_id):
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    success, frame = video_capture.read()
    
    if not success:
        raise Exception("Could not read from video")
    
    return frame

# assumes that the path is a path to a directory
def combine_timestamps(slide_transitions, frames, slides_json):
    comparator = ImageComparator()
    slides_info = json.loads(slides_json)
    slides = slides_info["slides"]
    num_slides = slides_info["num_slides"]
    timestamps = []
    frame_index = 0
    next_frame_to_merge = 0
    for slide_index in range(len(slides)):
        if (len(frames) - 1 - frame_index == num_slides - 1 - slide_index):
            while frame_index < len(frames):
                timestamps.append(slide_transitions[frame_index])
                frame_index +=1
            break
        
        while frame_index < len(frames):
            frame_path = frames[frame_index]
            score = comparator.get_similarity_score(slides[slide_index], frame_path)
            if (score[0] > 0.8):
                frame_index+=1
            else:
                second_score = comparator.get_similarity_score(slides[slide_index+1], frame_path)
                if (score > second_score):
                    frame_index+=1
                else:
                    break
        
        start1, _ = slide_transitions[next_frame_to_merge]
        _, end2 = slide_transitions[frame_index - 1]
        timestamps.append((start1, end2))
        next_frame_to_merge = frame_index
    
    return timestamps

# Identifies the initial timestamp of each slide, taken from a video
def get_initial_slide_timestamps(video_path, slides_json):
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
    
    # Map the dictionary values to be the start and end timestamp of the slide in seconds
    slide_transitions.pop(-1, None)
    frame_paths = []
    for slide_no, (start, end) in slide_transitions.items():
        frame = crop_frame(get_frame(cap, start), *bounding_box)
        frame_path = f"frames/cropped_frame{slide_no}.png"
        cv2.imwrite(frame_path, frame)
        frame_paths.append(frame_path)
        slide_transitions[slide_no] = (start / fps, end / fps)
    
    combined_timestamps = combine_timestamps(slide_transitions, frame_paths, slides_json) 
    
    return True, combined_timestamps

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
    result, slide_timestamps = get_initial_slide_timestamps("video.mp4", slides_json)
    if result:
        print(slide_timestamps)
    else:
        print("Fetching slide timestamps failed")