
import os 
from slide_squashing import squash_slides
from slide_timestamping import *
from split_pdf import convert_pdf_to_png


def get_timestamps(video_path, slides_path):
    slides_json = {}
    timestamps = {}
    if slides_path:
        output = slides_path.split('.')[0] + "/"
        os.mkdir(output)

        slides_json = convert_pdf_to_png(slides_path, output)
        squashed_json = squash_slides(slides_json)
        result, timestamps = get_slide_timestamps(video_path, squashed_json)
    else:
        result, slide_transitions, frame_paths = get_slide_timestamps(video_path, slides_json)
        slides_json = {
            "num_slides": len(frame_paths),
            "slides": frame_paths
        }
        squashed_json = squash_slides(slides_json)
        timestamps = match_frames(slide_transitions, frame_paths, squashed_json)

    # squashed_json = squash_slides(slides_json)

    if result:
        print(timestamps)

    else:
        print("Fetching slide timestamps failed")



get_timestamps("/vol/bitbucket/dme21/summentia-back/test_videos/gradient_descent.mp4", "")
# S:\Work\Coding\summentia-data\slides.pdf