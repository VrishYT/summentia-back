import hug
from falcon import HTTP_200
import json
from slide_timestamping import *
from split_pdf import convert_pdf_to_png
from audio_extractor import extract_audio
from audio_transcriber import get_transcripts_from_segments

import slide_api
import audio_api

api = hug.API(__name__)

@hug.response_middleware()
def process_response(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
    
# @hug.extend_api('/slides')
# def slide_api():
#     return [slide_api]

# @hug.extend_api('/audio')
# def audio_api():
#     return [audio_api]

@hug.post('/get_timestamps')
def get_timestamps(video_path, slides_path):
    slides_json = convert_pdf_to_png(slides_path, slides_path.split('.')[0])
    
    
@hug.post('/pipeline')
def pipeline(video_path, slides_path):
    # handle slides to get timestamps
    slides_json = convert_pdf_to_png(slides_path, slides_path.split('.')[0])
    _, timestamps = get_slide_timestamps(video_path, slides_json)
    # use timestamps to split audio in video 
    file_count = len(timestamps)
    timestamps.pop()
    frame_options = ','.join([str(t['end']) for t in timestamps])
    # use Whisper to transcribe audio   
    extract_audio(video_path, frame_options)
    transcripts = get_transcripts_from_segments(file_count, 0)
    print(transcripts)
    
    
# @hug.get('/happy')
# def happy_test():
#     # car = requests.get('http://localhost:8000/slides/hello')
#     car = slide_api.test_hello()
#     print(car)
#     hug.redirect.temporary('/slides/hello')
#     hug.redirect.to('/audio/hello')
    
@hug.post('/transcribe')
def transcribe_video(video_path, slides_json):
    _, timestamps = get_slide_timestamps(video_path, slides_json)
    file_count = len(timestamps)
    timestamps.pop()
    frame_options = ','.join([str(t['end']) for t in timestamps])
    
    extract_audio(video_path, frame_options)
    transcripts = get_transcripts_from_segments(file_count, 0)
    print(transcripts)
    
# if __name__ == '__main__':
#     slides_json = """{
#         "num_slides": 7,
#         "slides": [
#             "slides/Slides - Module 2 - K-NN and Decision Trees-01.png",
#             "slides/Slides - Module 2 - K-NN and Decision Trees-02.png",
#             "slides/Slides - Module 2 - K-NN and Decision Trees-03.png",
#             "slides/Slides - Module 2 - K-NN and Decision Trees-04.png",
#             "slides/Slides - Module 2 - K-NN and Decision Trees-05.png",
#             "slides/Slides - Module 2 - K-NN and Decision Trees-06.png",
#             "slides/Slides - Module 2 - K-NN and Decision Trees-07.png"
#         ]
#     }
#     """
#     transcribe_video("video.mp4", slides_json)

# print("https://localhost:8000")
# @hug.post('/get_timestamps')
# def get_timestamps(video_path, slides_json):
#     result, slide_timestamps = get_slide_timestamps(video_path, slides_json)
    
#     if result:
#         return {'data': json.dumps(slide_timestamps)}
#     else:
#         return "Fetching slide timestamps failed"
    