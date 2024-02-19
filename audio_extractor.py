import ffmpeg

def extract_audio(video_path, timestamps):
    # timestamps string should be passed as a comma separated list of frames, no spaces
    try:
        # ffmpeg.input(video_path).output('video_%03d.mp3', audio_bitrate='96k', map='0', f='segment', segment_start_number='1', segment_frames=timestamps).run()
        input = ffmpeg.input(video_path)
        out = input.output('video_%03d.mp3', audio_bitrate='96k', map='0', f='segment', segment_start_number='1', segment_frames=timestamps)
        out.run(capture_stdout = True, capture_stderr = True)
    except ffmpeg.Error as err:
        # print()
        # print('stdout:', err.stdout.decode('utf8'))
        # print()
        # print('stderr:', err.stderr.decode('utf8'))
        # print('\n\nEND OF STUFF\n\n')
        raise err
        
    

if __name__ == "__main__":
    extract_audio('video.mp4', '2000,3000,4000')