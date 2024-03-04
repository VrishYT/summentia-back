import shutil
import hug
import falcon
import json
from slide_squashing import squash_slides
from slide_timestamping import *
from split_pdf import convert_pdf_to_png
from audio_extractor import extract_audio, extract_single_audio
from audio_transcriber import get_transcripts_from_segments, transcribe

api = hug.API(__name__)

@hug.response_middleware()
def process_response(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

# @hug.post('/get_timestamps')
# def get_timestamps(video_path, slides_path):
#     slides_json = convert_pdf_to_png(slides_path, slides_path.split('.')[0])
    
@hug.get()
def handshake():
    print("Handshake completed.")
    return True
    
@hug.post('/process_slides')
def process_slides(project_folder, response):
    # handle slides to get timestamps
    slides_folder = os.path.join(project_folder, "slides/")
    if os.path.exists(slides_folder) and os.path.isdir(slides_folder):
        shutil.rmtree(slides_folder)
    os.mkdir(slides_folder)

    slides_path = os.path.join(project_folder, "slides.pdf")
    slides_json = convert_pdf_to_png(slides_path, slides_folder)
    squashed_json = squash_slides(slides_json)

    video_path = os.path.join(project_folder, "video.mp4")
    success, timestamps, num_frames = get_slide_timestamps(video_path, squashed_json, project_folder)
    if not success:
        response.status = falcon.get_http_status(400)
        return

    # use timestamps to split audio in video 
    file_count = len(timestamps)
    timestamps.pop()
    frame_options = ','.join([str(t['end']) for t in timestamps])
    # use Whisper to transcribe audio   
    extract_audio(video_path, frame_options)
    transcripts = get_transcripts_from_segments(file_count, 0)
    return transcripts

@hug.post('/process_noslides')
def process_noslides(project_folder):
    print(f"Processing {project_folder}...")
    audio_path = extract_single_audio(project_folder)
    print(f"Audio extracted.")
    transcript = transcribe(audio_path)
    print("Transcription complete.")
    return transcript

@hug.post('/process_genslides')
def process_noslides(video_path):
    pass
    
@hug.post('/transcribe')
def transcribe_video(video_path, slides_json):
    _, timestamps = get_slide_timestamps(video_path, slides_json)
    file_count = len(timestamps)
    timestamps.pop()
    frame_options = ','.join([str(t['end']) for t in timestamps])
    
    extract_audio(video_path, frame_options)
    transcripts = get_transcripts_from_segments(file_count, 0)
    print(transcripts)