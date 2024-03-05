
import os 
from slide_squashing import squash_slides
from slide_timestamping import *
from split_pdf import convert_pdf_to_png


def generate_slides(video_path):
    # timestamps = {}
    # result, slide_transitions, frame_paths = get_slide_timestamps(video_path, None)
    frames = ['frames/cropped_frame0.png', 'frames/cropped_frame1.png', 'frames/cropped_frame2.png', 
     'frames/cropped_frame3.png', 'frames/cropped_frame4.png', 'frames/cropped_frame5.png', 
     'frames/cropped_frame6.png', 'frames/cropped_frame7.png', 'frames/cropped_frame8.png', 
     'frames/cropped_frame9.png', 'frames/cropped_frame10.png', 'frames/cropped_frame11.png', 
     'frames/cropped_frame12.png', 'frames/cropped_frame13.png', 'frames/cropped_frame14.png', 
     'frames/cropped_frame15.png', 'frames/cropped_frame16.png', 'frames/cropped_frame17.png', 
     'frames/cropped_frame18.png', 'frames/cropped_frame19.png', 'frames/cropped_frame20.png', 
     'frames/cropped_frame21.png', 'frames/cropped_frame22.png', 'frames/cropped_frame23.png', 
     'frames/cropped_frame24.png', 'frames/cropped_frame25.png', 'frames/cropped_frame26.png', 
     'frames/cropped_frame27.png', 'frames/cropped_frame28.png', 'frames/cropped_frame29.png', 
     'frames/cropped_frame30.png', 'frames/cropped_frame31.png', 'frames/cropped_frame32.png', 
     'frames/cropped_frame33.png', 'frames/cropped_frame34.png', 'frames/cropped_frame35.png', 
     'frames/cropped_frame36.png', 'frames/cropped_frame37.png', 'frames/cropped_frame38.png', 
     'frames/cropped_frame39.png', 'frames/cropped_frame40.png', 'frames/cropped_frame41.png', 
     'frames/cropped_frame42.png', 'frames/cropped_frame43.png', 'frames/cropped_frame44.png', 
     'frames/cropped_frame45.png', 'frames/cropped_frame46.png', 'frames/cropped_frame47.png', 
     'frames/cropped_frame48.png', 'frames/cropped_frame49.png', 'frames/cropped_frame50.png', 
     'frames/cropped_frame51.png', 'frames/cropped_frame52.png', 'frames/cropped_frame53.png', 
     'frames/cropped_frame54.png', 'frames/cropped_frame55.png', 'frames/cropped_frame56.png', 
     'frames/cropped_frame57.png', 'frames/cropped_frame58.png', 'frames/cropped_frame59.png', 
     'frames/cropped_frame60.png', 'frames/cropped_frame61.png', 'frames/cropped_frame62.png', 
     'frames/cropped_frame63.png', 'frames/cropped_frame64.png', 'frames/cropped_frame65.png', 
     'frames/cropped_frame66.png', 'frames/cropped_frame67.png', 'frames/cropped_frame68.png', 
     'frames/cropped_frame69.png', 'frames/cropped_frame70.png', 'frames/cropped_frame71.png', 
     'frames/cropped_frame72.png', 'frames/cropped_frame73.png', 'frames/cropped_frame74.png', 
     'frames/cropped_frame75.png', 'frames/cropped_frame76.png', 'frames/cropped_frame77.png', 
     'frames/cropped_frame78.png', 'frames/cropped_frame79.png', 'frames/cropped_frame80.png', 
     'frames/cropped_frame81.png', 'frames/cropped_frame82.png', 'frames/cropped_frame83.png', 
     'frames/cropped_frame84.png', 'frames/cropped_frame85.png', 'frames/cropped_frame86.png', 
     'frames/cropped_frame87.png', 'frames/cropped_frame88.png', 'frames/cropped_frame89.png', 
     'frames/cropped_frame90.png', 'frames/cropped_frame91.png', 'frames/cropped_frame92.png', 
     'frames/cropped_frame93.png', 'frames/cropped_frame94.png', 'frames/cropped_frame95.png', 
     'frames/cropped_frame96.png', 'frames/cropped_frame97.png', 'frames/cropped_frame98.png', 
     'frames/cropped_frame99.png', 'frames/cropped_frame100.png', 'frames/cropped_frame101.png', 
     'frames/cropped_frame102.png', 'frames/cropped_frame103.png', 'frames/cropped_frame104.png', 
     'frames/cropped_frame105.png', 'frames/cropped_frame106.png', 'frames/cropped_frame107.png', 
     'frames/cropped_frame108.png', 'frames/cropped_frame109.png', 'frames/cropped_frame110.png', 
     'frames/cropped_frame111.png', 'frames/cropped_frame112.png', 'frames/cropped_frame113.png', 
     'frames/cropped_frame114.png', 'frames/cropped_frame115.png', 'frames/cropped_frame116.png', 
     'frames/cropped_frame117.png', 'frames/cropped_frame118.png', 'frames/cropped_frame119.png', 
     'frames/cropped_frame120.png', 'frames/cropped_frame121.png', 'frames/cropped_frame122.png', 
     'frames/cropped_frame123.png', 'frames/cropped_frame124.png', 'frames/cropped_frame125.png', 
     'frames/cropped_frame126.png', 'frames/cropped_frame127.png', 'frames/cropped_frame128.png', 
     'frames/cropped_frame129.png', 'frames/cropped_frame130.png', 'frames/cropped_frame131.png', 
     'frames/cropped_frame132.png', 'frames/cropped_frame133.png']
    
    slides_json = {
        "num_slides": len(frames),
        "slides": frames
    }
    squashed_json = squash_slides(slides_json)
    print(squashed_json)

    
generate_slides("test_videos/gradient_descent.mp4")