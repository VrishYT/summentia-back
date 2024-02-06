import itertools

import numpy as np
import cv2

from face_detection import FaceDetector
import SliTraNet.slide_detection_2d as SliTraNet

# Calculate the x coordinates that have been cropped to not include x1 and x2
def get_cropped_x_coords(x0, x1, frame_x0=0, frame_x1=852):
    x0_difference = abs(x0 - frame_x0)
    x1_difference = abs(x1 - frame_x1)
    
    padding = 100
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
    return np.array([x0, 0, x1, cap.get(cv2.CAP_PROP_FRAME_HEIGHT)])

# Identifies the initial timestamp of each slide, taken from a video
def get_initial_slide_timestamps(video_path):
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
    for slide_no, (start, end) in slide_transitions.items():
        slide_transitions[slide_no] = (start / fps, end / fps)
    
    return True, slide_transitions

# if __name__ == "__main__":
#     result, slide_timestamps = get_initial_slide_timestamps("video.mp4")
    
#     if result:
#         print(slide_timestamps)
#     else:
#         print("Fetching slide timestamps failed")