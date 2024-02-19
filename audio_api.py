import hug
from falcon import HTTP_200
import json
from audio_extractor import extract_audio

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
