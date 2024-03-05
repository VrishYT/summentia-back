from slide_timestamping import *


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

# slides_info = {'num_slides': 134, 
#      'slides': [{'path': 'frames/cropped_frame0.png', 'squashed': False}, {'path': 'frames/cropped_frame1.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame2.png', 'squashed': True}, {'path': 'frames/cropped_frame3.png', 'squashed': False}, 
#                 {'path': 'frames/cropped_frame4.png', 'squashed': True}, {'path': 'frames/cropped_frame5.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame6.png', 'squashed': True}, {'path': 'frames/cropped_frame7.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame8.png', 'squashed': True}, {'path': 'frames/cropped_frame9.png', 'squashed': False}, 
#                 {'path': 'frames/cropped_frame10.png', 'squashed': False}, {'path': 'frames/cropped_frame11.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame12.png', 'squashed': True}, {'path': 'frames/cropped_frame13.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame14.png', 'squashed': True}, {'path': 'frames/cropped_frame15.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame16.png', 'squashed': True}, {'path': 'frames/cropped_frame17.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame18.png', 'squashed': True}, {'path': 'frames/cropped_frame19.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame20.png', 'squashed': True}, {'path': 'frames/cropped_frame21.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame22.png', 'squashed': True}, {'path': 'frames/cropped_frame23.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame24.png', 'squashed': True}, {'path': 'frames/cropped_frame25.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame26.png', 'squashed': True}, {'path': 'frames/cropped_frame27.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame28.png', 'squashed': True}, {'path': 'frames/cropped_frame29.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame30.png', 'squashed': True}, {'path': 'frames/cropped_frame31.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame32.png', 'squashed': True}, {'path': 'frames/cropped_frame33.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame34.png', 'squashed': True}, {'path': 'frames/cropped_frame35.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame36.png', 'squashed': True}, {'path': 'frames/cropped_frame37.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame38.png', 'squashed': True}, {'path': 'frames/cropped_frame39.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame40.png', 'squashed': True}, {'path': 'frames/cropped_frame41.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame42.png', 'squashed': True}, {'path': 'frames/cropped_frame43.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame44.png', 'squashed': True}, {'path': 'frames/cropped_frame45.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame46.png', 'squashed': True}, {'path': 'frames/cropped_frame47.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame48.png', 'squashed': True}, {'path': 'frames/cropped_frame49.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame50.png', 'squashed': True}, {'path': 'frames/cropped_frame51.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame52.png', 'squashed': True}, {'path': 'frames/cropped_frame53.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame54.png', 'squashed': True}, {'path': 'frames/cropped_frame55.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame56.png', 'squashed': True}, {'path': 'frames/cropped_frame57.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame58.png', 'squashed': True}, {'path': 'frames/cropped_frame59.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame60.png', 'squashed': True}, {'path': 'frames/cropped_frame61.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame62.png', 'squashed': True}, {'path': 'frames/cropped_frame63.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame64.png', 'squashed': True}, {'path': 'frames/cropped_frame65.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame66.png', 'squashed': True}, {'path': 'frames/cropped_frame67.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame68.png', 'squashed': True}, {'path': 'frames/cropped_frame69.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame70.png', 'squashed': True}, {'path': 'frames/cropped_frame71.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame72.png', 'squashed': True}, {'path': 'frames/cropped_frame73.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame74.png', 'squashed': True}, {'path': 'frames/cropped_frame75.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame76.png', 'squashed': True}, {'path': 'frames/cropped_frame77.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame78.png', 'squashed': True}, {'path': 'frames/cropped_frame79.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame80.png', 'squashed': True}, {'path': 'frames/cropped_frame81.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame82.png', 'squashed': True}, {'path': 'frames/cropped_frame83.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame84.png', 'squashed': True}, {'path': 'frames/cropped_frame85.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame86.png', 'squashed': True}, {'path': 'frames/cropped_frame87.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame88.png', 'squashed': True}, {'path': 'frames/cropped_frame89.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame90.png', 'squashed': True}, {'path': 'frames/cropped_frame91.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame92.png', 'squashed': True}, {'path': 'frames/cropped_frame93.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame94.png', 'squashed': True}, {'path': 'frames/cropped_frame95.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame96.png', 'squashed': True}, {'path': 'frames/cropped_frame97.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame98.png', 'squashed': True}, {'path': 'frames/cropped_frame99.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame100.png', 'squashed': True}, {'path': 'frames/cropped_frame101.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame102.png', 'squashed': True}, {'path': 'frames/cropped_frame103.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame104.png', 'squashed': True}, {'path': 'frames/cropped_frame105.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame106.png', 'squashed': True}, {'path': 'frames/cropped_frame107.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame108.png', 'squashed': True}, {'path': 'frames/cropped_frame109.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame110.png', 'squashed': True}, {'path': 'frames/cropped_frame111.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame112.png', 'squashed': True}, {'path': 'frames/cropped_frame113.png', 'squashed': False}, 
#                 {'path': 'frames/cropped_frame114.png', 'squashed': False}, {'path': 'frames/cropped_frame115.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame116.png', 'squashed': False}, {'path': 'frames/cropped_frame117.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame118.png', 'squashed': True}, {'path': 'frames/cropped_frame119.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame120.png', 'squashed': False}, {'path': 'frames/cropped_frame121.png', 'squashed': False}, 
#                 {'path': 'frames/cropped_frame122.png', 'squashed': True}, {'path': 'frames/cropped_frame123.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame124.png', 'squashed': False}, {'path': 'frames/cropped_frame125.png', 'squashed': False}, 
#                 {'path': 'frames/cropped_frame126.png', 'squashed': True}, {'path': 'frames/cropped_frame127.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame128.png', 'squashed': True}, {'path': 'frames/cropped_frame129.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame130.png', 'squashed': True}, {'path': 'frames/cropped_frame131.png', 'squashed': True}, 
#                 {'path': 'frames/cropped_frame132.png', 'squashed': True}, {'path': 'frames/cropped_frame133.png', 'squashed': False}]}
    
transitions = {0: (1, 296), 1: (314, 3214), 2: (3228, 3561), 3: (3562, 5913), 4: (5927, 8118), 
                   5: (8119, 10524), 6: (10540, 11001), 7: (11002, 12162), 8: (12178, 13070), 
                   9: (13071, 14148), 10: (14159, 16259), 11: (16310, 16318), 12: (16319, 16333), 
                   13: (16334, 16345), 14: (16388, 16396), 15: (16397, 16411), 16: (16412, 16423), 
                   17: (16466, 16474), 18: (16475, 16489), 19: (16490, 16501), 20: (16541, 16549), 
                   21: (16550, 16561), 22: (16562, 16579), 23: (16622, 16630), 24: (16631, 16645), 
                   25: (16646, 16657), 26: (16700, 16708), 27: (16709, 16723), 28: (16724, 16735), 
                   29: (16775, 16783), 30: (16784, 16795), 31: (16796, 16813), 32: (16856, 16864), 
                   33: (16865, 16879), 34: (16880, 16891), 35: (16934, 16942), 36: (16943, 16957), 
                   37: (16958, 16969), 38: (17012, 17020), 39: (17021, 17035), 40: (17036, 17047), 
                   41: (17087, 17095), 42: (17096, 17107), 43: (17108, 17125), 44: (17165, 17173), 
                   45: (17174, 17185), 46: (17186, 17203), 47: (17246, 17254), 48: (17255, 17269), 
                   49: (17270, 17281), 50: (17324, 17332), 51: (17333, 17347), 52: (17348, 17359), 
                   53: (17402, 17410), 54: (17411, 17425), 55: (17426, 17437), 56: (17477, 17485), 
                   57: (17486, 17497), 58: (17498, 17515), 59: (17555, 17563), 60: (17564, 17575), 
                   61: (17576, 17593), 62: (17633, 17641), 63: (17642, 17653), 64: (17654, 17671), 
                   65: (17714, 17722), 66: (17723, 17737), 67: (17738, 17749), 68: (17792, 17800), 
                   69: (17801, 17815), 70: (17816, 17827), 71: (17873, 17884), 72: (17885, 17899), 
                   73: (17951, 17962), 74: (17963, 17977), 75: (18026, 18034), 76: (18035, 18049), 
                   77: (18050, 18061), 78: (18122, 18133), 79: (18185, 18193), 80: (18194, 18202), 
                   81: (18203, 18217), 82: (18263, 18274), 83: (18275, 18289), 84: (18338, 18346), 
                   85: (18347, 18361), 86: (18362, 18373), 87: (18416, 18424), 88: (18425, 18439), 
                   89: (18440, 18451), 90: (18494, 18502), 91: (18503, 18517), 92: (18518, 18529), 
                   93: (18569, 18577), 94: (18578, 18589), 95: (18590, 18607), 96: (18650, 18658), 
                   97: (18659, 18673), 98: (18674, 18685), 99: (18728, 18736), 100: (18737, 18751), 
                   101: (18752, 18763), 102: (18806, 18814), 103: (18815, 18829), 104: (18830, 18841), 
                   105: (18881, 18889), 106: (18890, 18901), 107: (18902, 18919), 108: (18962, 18970), 
                   109: (18971, 18985), 110: (18986, 18997), 111: (19040, 19048), 112: (19049, 19063), 
                   113: (19064, 19073), 114: (19074, 23758), 115: (23759, 23789), 116: (23790, 26303), 
                   117: (26319, 30010), 118: (30016, 30024), 119: (30025, 30215), 120: (30216, 31318), 
                   121: (31334, 36264), 122: (36265, 36338), 123: (36339, 37911), 124: (37912, 41101), 
                   125: (41117, 42443), 126: (42455, 42464), 127: (42465, 42504), 128: (42505, 42720), 
                   129: (42721, 42733), 130: (42734, 43097), 131: (43098, 43107), 132: (43108, 44113), 
                   133: (44114, 45180)}


def generate_slides(project_folder, transitions, frames):
    slides_json = {
        "num_slides": len(frames),
        "slides": frames
    }
    slides_info = squash_slides(slides_json)

    squash_filter = [(idx, slide) for idx, slide in enumerate(slides_info["slides"]) if not bool(slide.get("squashed"))]    
    squashed_indexes = list(map(lambda slide: slide[0], squash_filter))
    squashed_transitions = list(map(lambda x : [{"start": transitions[x][0], "end": transitions[x][1]}], squashed_indexes))
    
    print(squashed_transitions)
    # slides = list(map(lambda slide: slide[1].get("path"), squash_filter))
    # print(slides)

    slides_out = []
    cap = cv2.VideoCapture(os.path.join(project_folder, "video.mp4"))
    slides_folder = os.path.join(project_folder, "slides/")
    i=0
    if not (os.path.exists(slides_folder) and os.path.isdir(slides_folder)):
        os.mkdir(slides_folder)
    for transitions in squashed_transitions:
        frame_id = (transitions[0]["start"] + transitions[0]["end"])//2
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        ret, frame = cap.read()
        print(frame)
        slide_path = os.path.join(slides_folder, f"slide_{i}.png")
        cv2.imwrite(slide_path, frame)
        slides_out.append({
            "path": slide_path,
            "squashed": False
        })
        i+=1
        
    print(f"slides out: {slides_out}")
    print(F"squashed transitions: {squashed_transitions}")
    return slides_out, squashed_transitions

generate_slides("./project/", transitions, frames)