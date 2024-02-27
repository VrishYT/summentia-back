import hug
from falcon import HTTP_200
import json

import slide_api
import audio_api


api = hug.API(__name__)

@hug.response_middleware()
def process_response(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
    
@hug.extend_api('/slides')
def slide_api():
    return [slide_api]

@hug.extend_api('/audio')
def audio_api():
    return [audio_api]

# print("https://localhost:8000")
# @hug.post('/get_timestamps')
# def get_timestamps(video_path, slides_json):
#     result, slide_timestamps = get_slide_timestamps(video_path, slides_json)
    
#     if result:
#         return {'data': json.dumps(slide_timestamps)}
#     else:
#         return "Fetching slide timestamps failed"
    
# @hug.post('/get_timestamps')
# def get_timestamps(video_path, slides_path):
#     slides_json = convert_pdf_to_png(slides_path, slides_path.split('.')[0])
    
    
print("https://localhost:8000")
