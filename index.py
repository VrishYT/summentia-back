import hug
import json

from slide_timestamping import *

@hug.post('/get_timestamps')
def get_timestamps(video_path, slides_json):
    result, slide_timestamps = get_slide_timestamps(video_path, slides_json)
    
    if result:
        return json.dumps(slide_timestamps)
    else:
        return "Fetching slide timestamps failed"

print("https://localhost:8000")