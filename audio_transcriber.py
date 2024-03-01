from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

def get_transcripts_from_segments(file_count, out_index=0):
    transcripts = {}
    
    for i in range(out_index, file_count + out_index):
        output = ""
        segments, info = model.transcribe("video_" + str(i).zfill(3) + ".mp3", beam_size=5)

        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

        for segment in segments:
            # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
            output += segment.text
            
        transcripts[i] = output
    
    return transcripts
        
if __name__ == "__main__":
    get_transcripts_from_segments(7, 0)