import os
import ffmpeg

def extract_audio(project_folder, video_path, timestamps, out_index=0):
    # timestamps string should be passed as a comma separated list of frames, no spaces
    try:
        # ffmpeg.input(video_path).output('video_%03d.mp3', audio_bitrate='96k', map='0', f='segment', segment_start_number='1', segment_frames=timestamps).run()
        input = ffmpeg.input(video_path)
        out = input.output(os.path.join(project_folder, "%03d.mp3"), audio_bitrate='96k', map='0', f='segment', segment_start_number=str(out_index), segment_frames=timestamps)
        out.run(capture_stdout = True, capture_stderr = True)
        
    except ffmpeg.Error as err:
        raise err

def extract_single_audio(project_folder):
    try:
        mp3_path = os.path.join(project_folder, "audio.mp3")
        if os.path.exists(mp3_path):
            print(f"Deleting {mp3_path}...")
            os.unlink(mp3_path)

        input = ffmpeg.input(os.path.join(project_folder, "video.mp4"))
        out = input.output(mp3_path, audio_bitrate='96k')
        out.run(capture_stdout = True, capture_stderr = True)
        return mp3_path
    except ffmpeg.Error as err:
        raise err
    