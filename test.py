import os 
from slide_squashing import squash_slides
from split_pdf import convert_pdf_to_png


def get_timestamps(video_path, slides_path):
    output = slides_path.split('.')[0] + "/"
    os.mkdir(output)
    slides_json = convert_pdf_to_png(slides_path, output)
    squashed_json = squash_slides(slides_json)



get_timestamps("", "/mnt/s/Work/Coding/summentia-data/slides.pdf")
# S:\Work\Coding\summentia-data\slides.pdf