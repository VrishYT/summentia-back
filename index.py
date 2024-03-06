import shutil
from collections import OrderedDict

import falcon
import hug

from audio_extractor import extract_audio, extract_single_audio
from audio_transcriber import get_transcripts_from_segments, transcribe
from slide_timestamping import *
from split_pdf import convert_pdf_to_png

api = hug.API(__name__)


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
    success, transitions, frames = get_slide_timestamps(video_path, project_folder)
    if not success:
        response.status = falcon.get_http_status(400)
        return

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

    # use Whisper to transcribe audio
    extract_audio(project_folder, video_path, frame_options)

    transcripts = get_transcripts_from_segments(project_folder, len(keys), 0)

    slide_nos = list(timestamp_to_slide.values())

    slides_data = {}
    slides = squashed_json.get("slides")

    for i, transcript in enumerate(transcripts):
        slide_no = slide_nos[i]
        if slide_no in slides_data:
            data = slides_data[slide_no]
            print(data)
            data["transcript"].append(transcript)
            print(data["transcript"])
            slides_data[slide_no] = data
        else:
            squashed_info = slides[slide_no]
            slides_data[slide_no] = {
                "slide": squashed_info.get('path'),
                "transcript": [transcript],
                "summary": [],
                "squashed": squashed_info.get('squashed')
            }

    return slides_data


@hug.post('/process_noslides')
def process_noslides(project_folder):
    print(f"Processing {project_folder}.")
    audio_path = extract_single_audio(project_folder)
    print(f"Audio extracted.")
    transcript = transcribe(audio_path)
    print("Transcription complete.")
    return transcript


@hug.post('/process_genslides')
def process_genslides(project_folder, response):
    video_path = os.path.join(project_folder, "video.mp4")
    success, transitions, frames = get_slide_timestamps(video_path, project_folder)
    if not success:
        response.status = falcon.get_http_status(400)
        return

    slides_json, timestamps = generate_slides(project_folder, transitions, frames)

    timestamp_to_slide = {}

    num_slides = slides_json.get("num_slides")

    for slide_no in range(num_slides):
        for segment in timestamps[slide_no]:
            end_frame = segment["end"]
            timestamp_to_slide[str(end_frame)] = int(slide_no)

    sorted_dict = OrderedDict(sorted(timestamp_to_slide.items(), key=lambda x: int(x[0])))
    keys = sorted_dict.keys()
    frame_options = ','.join(keys)

    # use Whisper to transcribe audio
    extract_audio(project_folder, video_path, frame_options)

    transcripts = get_transcripts_from_segments(project_folder, len(keys), 0)
    slide_nos = list(timestamps.values())

    slides_data = {}
    slides = slides_json.get("slides")

    for i, transcript in enumerate(transcripts):
        slide_no = slide_nos[i]
        if slide_no in slides_data:
            data = slides_data[slide_no]
            print(data)
            data["transcript"].append(transcript)
            print(data["transcript"])
            slides_data[slide_no] = data
        else:
            squashed_info = slides[slide_no]
            slides_data[slide_no] = {
                "slide": squashed_info.get('path'),
                "transcript": [transcript],
                "summary": [],
                "squashed": squashed_info.get('squashed')
            }

    return slides_data
