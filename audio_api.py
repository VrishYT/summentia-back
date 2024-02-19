import hug
from falcon import HTTP_200
import json

@hug.get('/hello')
def test_hello():
  return {'data': "HELLO WORLD"}
  
@hug.post('/extract')
def extract_audio(video_path):
  pass
