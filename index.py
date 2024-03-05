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
    
    ## change timestamps format for extracting audio
    timestamp_to_slide = {}
    for slide in timestamps:
        # print(slide)
        for segment in timestamps[slide]:
            end_frame = segment["end"]
            timestamp_to_slide[str(end_frame)] = int(slide)
    print(timestamp_to_slide)
    
    temp = {}
    keys = list(timestamp_to_slide.keys())[:-1]
    frame_options = ','.join(keys)

    # use Whisper to transcribe audio   
    extract_audio(project_folder, video_path, frame_options)
    # transcripts = get_transcripts_from_segments(len(timestamp_to_slide), 0)
    transcripts = get_transcripts_from_segments(project_folder, len(timestamp_to_slide), 0)
    
    return_list = []
    
    for slide_key, segments in timestamps.items():
        # get the slide image path and squashed variable 
        slide_index = int(slide_key) - 1
        slide_dict = squashed_json.get("slides")[slide_index]
        slide_path = slide_dict.get("path")
        slide_squashed = slide_dict.get("squashed")
        
        # get the timestamps
        temp_cnt = 0
        slide_transcripts = []
        for timestamp, slide in timestamp_to_slide:
            if str(slide) == slide_index:
                slide_transcripts.append(transcripts[temp_cnt])
            temp_cnt += 1
        
        # return the dictionary 
        transcript_dict = {
            "slide": slide_path,
            "transcript": slide_transcripts,
            "summary": [],
            "squashed": slide_squashed
        }
        return_list.append(transcript_dict)
    
    return return_list

# [{slide: (slide_img_path) string, transcripts : string[], summary: string[], squashed: bool}]

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