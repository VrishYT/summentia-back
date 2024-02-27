import hug
from falcon import HTTP_200
import json
from audio_extractor import extract_audio
from audio_transcriber import get_transcripts_from_segments

@hug.exception(Exception)
def exception_handler(exception):
  # print("\n\nEXCEPTION\n\n")
  # print(exception)
  # return {'error': exception }
  raise exception

@hug.get('/hello')
def test_hello():
  return {'data': "HELLO WORLD"}
  
@hug.post('/extract')
def extract(video_path, timestamps):
  extract_audio(video_path, timestamps)

@hug.post('/transcribe')
def transcribe(file_count):
  transcripts = get_transcripts_from_segments(int(file_count))
  return {'data': json.dumps(transcripts)}

@hug.post('/convert')
def convert_video_to_audio():
  try:
    extract_audio("video.mp4", "2000,3000,4000")
    transcripts = transcribe(4)
    return {'data': json.dumps(transcripts)}
    
  finally:
    pass