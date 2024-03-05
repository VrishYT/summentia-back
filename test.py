
import os 
from slide_squashing import squash_slides
from slide_timestamping import *
from split_pdf import convert_pdf_to_png


def generate_slides(video_path):
    timestamps = {}
    result, slide_transitions, frame_paths = get_slide_timestamps(video_path, None)
    slides_json = {
        "num_slides": len(frame_paths),
        "slides": frame_paths
    }
    squashed_json = squash_slides(slides_json)
    print(squashed_json)

    



generate_slides("test_videos/gradient_descent.mp4")