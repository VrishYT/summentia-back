import os
from faster_whisper import WhisperModel

model_size = "tiny.en"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

def get_transcripts_from_segments(project_folder, file_count, out_index=0):
    transcripts = []
    
    for i in range(out_index, file_count + out_index):
        output = ""
        segments, info = model.transcribe(os.path.join(os.path.join(project_folder, "audio/"), str(i).zfill(3) + ".mp3"), beam_size=5)

        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

        for segment in segments:
            # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
            output += segment.text
            
        transcripts.append(output)
    
    return transcripts

def transcribe(file_path):
    print(file_path)
    segments, info = model.transcribe(file_path, beam_size=5)
    print("1")
    # segments = list(segments)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    output = ""
    for segment in segments:
        output += segment.text

    return output