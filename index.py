import shutil
from collections import OrderedDict

import falcon
import hug

from audio_extractor import extract_audio, extract_single_audio
from audio_transcriber import get_transcripts_from_segments, transcribe
from slide_timestamping import *
from split_pdf import convert_pdf_to_png

api = hug.API(__name__)

PROJECTS_FOLDER = "/mnt/c/Users/gabde/Documents/Uni/Third Year/COMP60021/Summentia/projects"


@hug.response_middleware()
def process_response(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')


@hug.get()
def handshake():
    print("Handshake completed.")
    return True


@hug.post('/process_slides')
def process_slides(uuid, response):
    print(f"Processing slides for project uuid: {uuid}")
    # handle slides to get timestamps
    project_folder = os.path.join(PROJECTS_FOLDER, uuid)
    slides_folder = os.path.join(project_folder, "slides/")
    if os.path.exists(slides_folder) and os.path.isdir(slides_folder):
        shutil.rmtree(slides_folder)
    os.mkdir(slides_folder)
    
    
    print(f"Splitting pdf")

    slides_path = os.path.join(project_folder, "slides.pdf")
    slides_json = convert_pdf_to_png(slides_path, slides_folder)
    
    print(f"Squashing pdf")
    squashed_json = squash_slides(slides_json)

    print(f"Getting slide timestamps")
    video_path = os.path.join(project_folder, "video.mp4")
    success, transitions, frames = get_slide_timestamps(video_path, project_folder)
    if not success:
        response.status = falcon.get_http_status(400)
        return


    print(f"Matching frames")
    timestamps = match_frames(transitions, frames, squashed_json)

    timestamp_to_slide = {}

    num_slides = squashed_json.get("num_slides")

    for slide_no in range(num_slides):
        for segment in timestamps[slide_no]:
            end_frame = segment["end"]
            timestamp_to_slide[str(end_frame)] = int(slide_no)

    sorted_dict = OrderedDict(sorted(timestamp_to_slide.items(), key=lambda x: int(x[0])))
    keys = sorted_dict.keys()
    frame_options = ','.join(keys)


    print(f"Extracting audio")
    # use Whisper to transcribe audio
    extract_audio(project_folder, video_path, frame_options)



    print(f"Transcribing")
    transcripts = get_transcripts_from_segments(project_folder, len(keys), 0)

    slide_nos = list(timestamp_to_slide.values())

    slides_data = {}

    for i, slide in enumerate(squashed_json.get("slides")):
        slides_data[i] = {
            "slide": slide.get("path"),
            "transcripts": [],
            "summaries": [],
            "squashed": slide.get('squashed')
        }

    for i, transcript in enumerate(transcripts):
        slide_no = slide_nos[i]
        slide_data = slides_data[slide_no]
        slide_data["transcripts"].append(transcript)

    print(f"--- Done --- \n{slides_data}")
    return slides_data


@hug.post('/process_noslides')
def process_noslides(uuid):
    project_folder = os.path.join(PROJECTS_FOLDER, uuid)
    print(f"Processing {project_folder}.")
    audio_path = extract_single_audio(project_folder)
    print(f"Audio extracted.")
    transcript = transcribe(audio_path)
    print("Transcription complete.")
    return transcript


@hug.post('/process_genslides')
def process_genslides(uuid, response):
    print(f"Gen slides for project uuid: {uuid}")
    project_folder = os.path.join(PROJECTS_FOLDER, uuid)
    video_path = os.path.join(project_folder, "video.mp4")
    
    print(f"Getting slide timestamps")
    success, transitions, frames = get_slide_timestamps(video_path, project_folder)
    if not success:
        response.status = falcon.get_http_status(400)
        return

    print(f"Generating slides")
    slides, timestamps = generate_slides(project_folder, transitions, frames)

    timestamp_to_slide = {}

    num_slides = len(slides)

    for slide_no in range(num_slides):
        for segment in timestamps[slide_no]:
            end_frame = segment["end"]
            timestamp_to_slide[str(end_frame)] = int(slide_no)

    sorted_dict = OrderedDict(sorted(timestamp_to_slide.items(), key=lambda x: int(x[0])))
    keys = sorted_dict.keys()
    frame_options = ','.join(keys)

    print("Extracting audio")
    # use Whisper to transcribe audio
    extract_audio(project_folder, video_path, frame_options)

    print("Getting timestamps")
    transcripts = get_transcripts_from_segments(project_folder, len(keys), 0)
    slide_nos = list(timestamp_to_slide.values())

    slides_data = {}

    for i, transcript in enumerate(transcripts):
        slide_no = slide_nos[i]
        if slide_no in slides_data:
            data = slides_data[slide_no]
            print(data)
            data["transcripts"].append(transcript)
            print(data["transcripts"])
            slides_data[slide_no] = data
        else:
            squashed_info = slides[slide_no]
            slides_data[slide_no] = {
                "slide": squashed_info.get('path'),
                "transcripts": [transcript],
                "summaries": [],
                "squashed": squashed_info.get('squashed')
            }

    print(f"--- Done --- \n{slides_data}")
    return slides_data
