import os

import ffmpeg


def extract_audio(project_folder, video_path, timestamps, out_index=0):
    # timestamps string should be passed as a comma separated list of frames, no spaces
    try:
        input = ffmpeg.input(video_path)
        print("Got video path")
        audio_folder = os.path.join(project_folder, "audio/")
        if not (os.path.exists(audio_folder) and os.path.isdir(audio_folder)):
            os.mkdir(audio_folder)
        out = input.output(os.path.join(audio_folder, "%03d.mp3"), audio_bitrate='96k', f='segment',
                           segment_start_number=str(out_index), segment_frames=timestamps)
        print("Segmenting audio")
        out.run(capture_stdout=True, capture_stderr=True)
        print("Segmented audio successfully")

    except ffmpeg.Error as err:
        print(f"Error segmenting audio: {err.stderr}")
        raise err


def extract_single_audio(project_folder):
    try:
        mp3_path = os.path.join(project_folder, "audio.mp3")
        if os.path.exists(mp3_path):
            print(f"Deleting {mp3_path}...")
            os.unlink(mp3_path)

        input = ffmpeg.input(os.path.join(project_folder, "video.mp4"))
        out = input.output(mp3_path, audio_bitrate='96k')
        out.run(capture_stdout=True, capture_stderr=True)
        print(mp3_path)
        return mp3_path
    except ffmpeg.Error as err:
        raise err
