import hug

from slide_timestamping import *

@hug.get('/get_timestamps')
def get_timestamps(video_path, slides_json):
    result, slide_timestamps = get_slide_timestamps(video_path, slides_json)
    
    if result:
        return slide_timestamps
    else:
        return "Fetching slide timestamps failed"

print("https://localhost:8000")