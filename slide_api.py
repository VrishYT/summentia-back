import hug
from falcon import HTTP_200
import json
from slide_timestamping import *
from split_pdf import convert_pdf_to_png

@hug.get('/hello')
def test_hello():
    return {'data': "HELLO WORLD"}

# @hug.post('/get_timestamps')
# def get_timestamps(video_path, slides_json):
#     result, slide_timestamps = get_slide_timestamps(video_path, slides_json)
    
#     if result:
#         return {'data': json.dumps(slide_timestamps)}
#     else:
#         return "Fetching slide timestamps failed"
    
    
@hug.post('/get_timestamps')
def get_timestamps(video_path, slides_path):
    slides_json = convert_pdf_to_png(slides_path, slides_path.split('.')[0])
