from slide_squashing import squash_slides
from split_pdf import convert_pdf_to_png
from slide_timestamping import get_slide_timestamps, match_frames
gradient_slides_json = convert_pdf_to_png("test_slide_pdfs/gradient_descent_slides.pdf", "test_slides/gradient_descent/output_image")
slides_info = squash_slides(gradient_slides_json)


# # psychology_slides_json = {
# #         "num_slides": 18,
# #         "slides": [
# #             "test_slides/intro_to_psychology/output_image_page_1.png",
# #             "test_slides/intro_to_psychology/output_image_page_2.png",
# #             "test_slides/intro_to_psychology/output_image_page_3.png",
# #             "test_slides/intro_to_psychology/output_image_page_4.png",
# #             "test_slides/intro_to_psychology/output_image_page_5.png",
# #             "test_slides/intro_to_psychology/output_image_page_6.png",
# #             "test_slides/intro_to_psychology/output_image_page_7.png",
# #             "test_slides/intro_to_psychology/output_image_page_8.png",
# #             "test_slides/intro_to_psychology/output_image_page_9.png",
# #             "test_slides/intro_to_psychology/output_image_page_10.png",
# #             "test_slides/intro_to_psychology/output_image_page_11.png",
# #             "test_slides/intro_to_psychology/output_image_page_12.png",
# #             "test_slides/intro_to_psychology/output_image_page_13.png",
# #             "test_slides/intro_to_psychology/output_image_page_14.png",
# #             "test_slides/intro_to_psychology/output_image_page_15.png",
# #             "test_slides/intro_to_psychology/output_image_page_16.png",
# #             "test_slides/intro_to_psychology/output_image_page_17.png",
# #             "test_slides/intro_to_psychology/output_image_page_18.png"
# #         ]
# #     }

# # kernel_design_json = {
# #         "num_slides": 17,
# #         "slides": [
# #             "test_slides/kernel_design/output_image_page_1.png",
# #             "test_slides/kernel_design/output_image_page_2.png",
# #             "test_slides/kernel_design/output_image_page_3.png",
# #             "test_slides/kernel_design/output_image_page_4.png",
# #             "test_slides/kernel_design/output_image_page_5.png",
# #             "test_slides/kernel_design/output_image_page_6.png",
# #             "test_slides/kernel_design/output_image_page_7.png",
# #             "test_slides/kernel_design/output_image_page_8.png",
# #             "test_slides/kernel_design/output_image_page_9.png",
# #             "test_slides/kernel_design/output_image_page_10.png",
# #             "test_slides/kernel_design/output_image_page_11.png",
# #             "test_slides/kernel_design/output_image_page_12.png",
# #             "test_slides/kernel_design/output_image_page_13.png",
# #             "test_slides/kernel_design/output_image_page_14.png",
# #             "test_slides/kernel_design/output_image_page_15.png",
# #             "test_slides/kernel_design/output_image_page_16.png",
# #             "test_slides/kernel_design/output_image_page_17.png"
# #         ]
# #     }

# reinforcement_json = {
#         "num_slides": 47,
#         "slides": [
#             "test_slides/reinforcement/output_image_page_1.png",
#             "test_slides/reinforcement/output_image_page_2.png",
#             "test_slides/reinforcement/output_image_page_3.png",
#             "test_slides/reinforcement/output_image_page_4.png",
#             "test_slides/reinforcement/output_image_page_5.png",
#             "test_slides/reinforcement/output_image_page_6.png",
#             "test_slides/reinforcement/output_image_page_7.png",
#             "test_slides/reinforcement/output_image_page_8.png",
#             "test_slides/reinforcement/output_image_page_9.png",
#             "test_slides/reinforcement/output_image_page_10.png",
#             "test_slides/reinforcement/output_image_page_11.png",
#             "test_slides/reinforcement/output_image_page_12.png",
#             "test_slides/reinforcement/output_image_page_13.png",
#             "test_slides/reinforcement/output_image_page_14.png",
#             "test_slides/reinforcement/output_image_page_15.png",
#             "test_slides/reinforcement/output_image_page_16.png",
#             "test_slides/reinforcement/output_image_page_17.png",
#             "test_slides/reinforcement/output_image_page_18.png",
#             "test_slides/reinforcement/output_image_page_19.png",
#             "test_slides/reinforcement/output_image_page_20.png",
#             "test_slides/reinforcement/output_image_page_21.png",
#             "test_slides/reinforcement/output_image_page_22.png",
#             "test_slides/reinforcement/output_image_page_23.png",
#             "test_slides/reinforcement/output_image_page_24.png",
#             "test_slides/reinforcement/output_image_page_25.png",
#             "test_slides/reinforcement/output_image_page_26.png",
#             "test_slides/reinforcement/output_image_page_27.png",
#             "test_slides/reinforcement/output_image_page_28.png",
#             "test_slides/reinforcement/output_image_page_29.png",
#             "test_slides/reinforcement/output_image_page_30.png",
#             "test_slides/reinforcement/output_image_page_31.png",
#             "test_slides/reinforcement/output_image_page_32.png",
#             "test_slides/reinforcement/output_image_page_33.png",
#             "test_slides/reinforcement/output_image_page_34.png",
#             "test_slides/reinforcement/output_image_page_35.png",
#             "test_slides/reinforcement/output_image_page_36.png",
#             "test_slides/reinforcement/output_image_page_37.png",
#             "test_slides/reinforcement/output_image_page_38.png",
#             "test_slides/reinforcement/output_image_page_39.png",
#             "test_slides/reinforcement/output_image_page_40.png",
#             "test_slides/reinforcement/output_image_page_41.png",
#             "test_slides/reinforcement/output_image_page_42.png",
#             "test_slides/reinforcement/output_image_page_43.png",
#             "test_slides/reinforcement/output_image_page_44.png",
#             "test_slides/reinforcement/output_image_page_45.png",
#             "test_slides/reinforcement/output_image_page_46.png",
#             "test_slides/reinforcement/output_image_page_47.png"
#         ]
#     }

english_history_json = {
        "num_slides": 45,
        "slides": [
            "test_slides/english_history/output_image_page_1.png",
            "test_slides/english_history/output_image_page_2.png",
            "test_slides/english_history/output_image_page_3.png",
            "test_slides/english_history/output_image_page_4.png",
            "test_slides/english_history/output_image_page_5.png",
            "test_slides/english_history/output_image_page_6.png",
            "test_slides/english_history/output_image_page_7.png",
            "test_slides/english_history/output_image_page_8.png",
            "test_slides/english_history/output_image_page_9.png",
            "test_slides/english_history/output_image_page_10.png",
            "test_slides/english_history/output_image_page_11.png",
            "test_slides/english_history/output_image_page_12.png",
            "test_slides/english_history/output_image_page_13.png",
            "test_slides/english_history/output_image_page_14.png",
            "test_slides/english_history/output_image_page_15.png",
            "test_slides/english_history/output_image_page_16.png",
            "test_slides/english_history/output_image_page_17.png",
            "test_slides/english_history/output_image_page_18.png",
            "test_slides/english_history/output_image_page_19.png",
            "test_slides/english_history/output_image_page_20.png",
            "test_slides/english_history/output_image_page_21.png",
            "test_slides/english_history/output_image_page_22.png",
            "test_slides/english_history/output_image_page_23.png",
            "test_slides/english_history/output_image_page_24.png",
            "test_slides/english_history/output_image_page_25.png",
            "test_slides/english_history/output_image_page_26.png",
            "test_slides/english_history/output_image_page_27.png",
            "test_slides/english_history/output_image_page_28.png",
            "test_slides/english_history/output_image_page_29.png",
            "test_slides/english_history/output_image_page_30.png",
            "test_slides/english_history/output_image_page_31.png",
            "test_slides/english_history/output_image_page_32.png",
            "test_slides/english_history/output_image_page_33.png",
            "test_slides/english_history/output_image_page_34.png",
            "test_slides/english_history/output_image_page_35.png",
            "test_slides/english_history/output_image_page_36.png",
            "test_slides/english_history/output_image_page_37.png",
            "test_slides/english_history/output_image_page_38.png",
            "test_slides/english_history/output_image_page_39.png",
            "test_slides/english_history/output_image_page_40.png",
            "test_slides/english_history/output_image_page_41.png",
            "test_slides/english_history/output_image_page_42.png",
            "test_slides/english_history/output_image_page_43.png",
            "test_slides/english_history/output_image_page_44.png",
            "test_slides/english_history/output_image_page_45.png",
        ]
    }

squashed_json = squash_slides(english_history_json)
print(f"squashed slides: {squashed_json}")

# # transitions = {0: (9, 1374), 1: (1379, 3290), 2: (3291, 3314), 3: (3327, 3370), 4: (3373, 4979), 5: (4980, 4990), 6: (4992, 5016), 
# #                7: (5017, 6359), 8: (6360, 6450), 9: (6451, 6728), 10: (6733, 8817), 11: (8818, 22796), 12: (22797, 32028), 
# #                13: (32029, 32342), 14: (32347, 32424), 15: (32428, 34632), 16: (34633, 40152), 17: (40153, 40204), 18: (40216, 40257), 
# #                19: (40264, 40272), 20: (40273, 41421), 21: (41422, 42873), 22: (42874, 42966), 23: (42967, 43042), 24: (43043, 44332), 
# #                25: (44333, 44510), 26: (44526, 44595), 27: (44598, 44674), 28: (44675, 44692), 29: (44695, 44765), 30: (44766, 44874), 
# #                31: (44877, 44885), 32: (44886, 46229), 33: (46230, 56226), 34: (56227, 56892), 35: (56893, 57044), 36: (57045, 57641), 
# #                37: (57648, 57858), 38: (57859, 58353), 39: (58354, 58362), 40: (58363, 58420), 41: (58423, 61156), 42: (61157, 61852), 
# #                43: (61853, 67770), 44: (67771, 68178), 45: (68179, 71963), 46: (71971, 72622), 47: (72623, 73259)}

# # frames = ['frames/cropped_frame0.png', 'frames/cropped_frame1.png', 'frames/cropped_frame2.png', 'frames/cropped_frame3.png', 
# #           'frames/cropped_frame4.png', 'frames/cropped_frame5.png', 'frames/cropped_frame6.png', 'frames/cropped_frame7.png', 
# #           'frames/cropped_frame8.png', 'frames/cropped_frame9.png', 'frames/cropped_frame10.png', 'frames/cropped_frame11.png', 
# #           'frames/cropped_frame12.png', 'frames/cropped_frame13.png', 'frames/cropped_frame14.png', 'frames/cropped_frame15.png', 
# #           'frames/cropped_frame16.png', 'frames/cropped_frame17.png', 'frames/cropped_frame18.png', 'frames/cropped_frame19.png', 
# #           'frames/cropped_frame20.png', 'frames/cropped_frame21.png', 'frames/cropped_frame22.png', 'frames/cropped_frame23.png', 
# #           'frames/cropped_frame24.png', 'frames/cropped_frame25.png', 'frames/cropped_frame26.png', 'frames/cropped_frame27.png', 
# #           'frames/cropped_frame28.png', 'frames/cropped_frame29.png', 'frames/cropped_frame30.png', 'frames/cropped_frame31.png', 
# #           'frames/cropped_frame32.png', 'frames/cropped_frame33.png', 'frames/cropped_frame34.png', 'frames/cropped_frame35.png', 
# #           'frames/cropped_frame36.png', 'frames/cropped_frame37.png', 'frames/cropped_frame38.png', 'frames/cropped_frame39.png', 
# #           'frames/cropped_frame40.png', 'frames/cropped_frame41.png', 'frames/cropped_frame42.png', 'frames/cropped_frame43.png', 
# #           'frames/cropped_frame44.png', 'frames/cropped_frame45.png', 'frames/cropped_frame46.png', 'frames/cropped_frame47.png']

# # transitions = {0: (3, 18), 1: (25, 70), 2: (71, 1880), 3: (1881, 4184), 4: (4185, 7127), 
# #                5: (7128, 7924), 6: (7925, 8013), 7: (8014, 11221), 8: (11222, 12223), 
# #                9: (12224, 13786), 10: (13787, 15266), 11: (15267, 16067), 12: (16068, 16252), 
# #                13: (16259, 16328), 14: (16329, 18178), 15: (18179, 19343), 16: (19344, 19837), 
# #                17: (19838, 20172), 18: (20173, 20720), 19: (20721, 21664), 20: (21665, 23064), 
# #                21: (23065, 23075)}
# # frames = ['frames/cropped_frame0.png', 'frames/cropped_frame1.png', 'frames/cropped_frame2.png', 
# #           'frames/cropped_frame3.png', 'frames/cropped_frame4.png', 'frames/cropped_frame5.png', 
# #           'frames/cropped_frame6.png', 'frames/cropped_frame7.png', 'frames/cropped_frame8.png', 
# #           'frames/cropped_frame9.png', 'frames/cropped_frame10.png', 'frames/cropped_frame11.png', 
# #           'frames/cropped_frame12.png', 'frames/cropped_frame13.png', 'frames/cropped_frame14.png', 
# #           'frames/cropped_frame15.png', 'frames/cropped_frame16.png', 'frames/cropped_frame17.png', 
# #           'frames/cropped_frame18.png', 'frames/cropped_frame19.png', 'frames/cropped_frame20.png', 
# #           'frames/cropped_frame21.png']


result, transitions, frames = get_slide_timestamps("test_videos/english_history.mp4", squashed_json)
if result:
    print(transitions)
    print(frames)
else:
    print("slide timestamping did not work for english history")

timestamps = match_frames(transitions, frames, squashed_json)
print(timestamps)