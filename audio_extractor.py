import ffmpeg

def extract_audio(video_path, timestamps):
    ffmpeg.input(video_path).output('video_%03d.mp3', audio_bitrate='96k', map='0', f='segment', segment_start_number='1', segment_frames='2000,3000,4000').run()

if __name__ == "__main__":
    extract_audio('video.mp4', {})