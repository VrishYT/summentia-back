from slide_squashing import squash_slides
from split_pdf import convert_pdf_to_png
from slide_timestamping import get_slide_timestamps, match_frames
#convert_pdf_to_png("test_slide_pdfs/english_history_slides.pdf", "test_slides/english_history/output_image")
# # gradient_slides_json = {
# #         "num_slides": 12,
# #         "slides": [
# #             "test_slides/gradient_descent/output_image_page_1.png",
# #             "test_slides/gradient_descent/output_image_page_2.png",
# #             "test_slides/gradient_descent/output_image_page_3.png",
# #             "test_slides/gradient_descent/output_image_page_4.png",
# #             "test_slides/gradient_descent/output_image_page_5.png",
# #             "test_slides/gradient_descent/output_image_page_6.png",
# #             "test_slides/gradient_descent/output_image_page_7.png",
# #             "test_slides/gradient_descent/output_image_page_8.png",
# #             "test_slides/gradient_descent/output_image_page_9.png",
# #             "test_slides/gradient_descent/output_image_page_10.png",
# #             "test_slides/gradient_descent/output_image_page_11.png",
# #             "test_slides/gradient_descent/output_image_page_12.png"
# #         ]
# #     }

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

# kernel_design_json = {
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

transitions = {0: (1, 565), 1: (566, 1117), 2: (1118, 1126), 3: (1133, 1245), 4: (1246, 1433), 5: (1434, 1631), 
 6: (1660, 1675), 7: (1676, 1701), 8: (1712, 1765), 9: (1766, 1837), 10: (1838, 2080), 11: (2081, 2354), 
 12: (2356, 2893), 13: (2894, 2937), 14: (2938, 2975), 15: (2976, 3088), 16: (3089, 3475), 17: (3476, 3487), 
 18: (3488, 3625), 19: (3626, 3640), 20: (3641, 4219), 21: (4220, 4329), 22: (4359, 4370), 23: (4383, 4394), 
 24: (4395, 4544), 25: (4545, 4582), 26: (4583, 4732), 27: (4733, 4768), 28: (4769, 4918), 29: (4919, 4957), 
 30: (4958, 5107), 31: (5108, 5131), 32: (5132, 5269), 33: (5270, 5522), 34: (5531, 5680), 35: (5681, 5695), 36: (5696, 5845), 
 37: (5853, 5989), 38: (5996, 6128), 39: (6135, 6292), 40: (6311, 6331), 41: (6332, 7171), 42: (7172, 8017), 43: (8018, 8867), 
 44: (8868, 9110), 45: (9111, 9721), 46: (9722, 10231), 47: (10233, 10519), 48: (10520, 10801), 49: (10802, 11144), 
 50: (11145, 11695), 51: (11697, 11782), 52: (11783, 11987), 53: (11988, 12086), 54: (12087, 12221), 55: (12222, 12596), 
 56: (12597, 12862), 57: (12890, 13011), 58: (13018, 13167), 59: (13168, 13185), 60: (13186, 13301), 61: (13302, 13313), 
 62: (13314, 13437), 63: (13438, 13447), 64: (13448, 13575), 65: (13576, 13681), 66: (13682, 13705), 67: (13706, 13811), 
 68: (13814, 13931), 69: (13936, 14049), 70: (14050, 14165), 71: (14166, 14315), 72: (14318, 14453), 73: (14456, 14591), 
 74: (14594, 14731), 75: (14760, 14906), 76: (14907, 15152), 77: (15153, 15362), 78: (15363, 15730), 79: (15731, 15884), 
 80: (15886, 15952), 81: (15971, 16112), 82: (16121, 16161), 83: (16162, 16621), 84: (16622, 16953), 85: (16954, 17077), 
 86: (17084, 17175), 87: (17176, 17277), 88: (17278, 17656), 89: (17675, 17713), 90: (17714, 17733), 91: (17734, 17944), 
 92: (17956, 18069), 93: (18070, 18079), 94: (18080, 18171), 95: (18172, 18181), 96: (18182, 18295), 97: (18302, 18429), 
 98: (18436, 18563), 99: (18568, 18663), 100: (18670, 18793), 101: (18794, 18929), 102: (18930, 18941), 103: (18942, 19047), 
 104: (19050, 19169), 105: (19172, 19271), 106: (19276, 19395), 107: (19396, 19535), 108: (19542, 19691), 109: (19712, 20282), 
 110: (20283, 21023), 111: (21024, 21079), 112: (21080, 21290), 113: (21291, 21634), 114: (21635, 22126), 115: (22127, 22481)}

frames = ['frames/cropped_frame0.png', 'frames/cropped_frame1.png', 'frames/cropped_frame2.png', 'frames/cropped_frame3.png', 
          'frames/cropped_frame4.png', 'frames/cropped_frame5.png', 'frames/cropped_frame6.png', 'frames/cropped_frame7.png', 
          'frames/cropped_frame8.png', 'frames/cropped_frame9.png', 'frames/cropped_frame10.png', 'frames/cropped_frame11.png', 
          'frames/cropped_frame12.png', 'frames/cropped_frame13.png', 'frames/cropped_frame14.png', 'frames/cropped_frame15.png', 
          'frames/cropped_frame16.png', 'frames/cropped_frame17.png', 'frames/cropped_frame18.png', 'frames/cropped_frame19.png', 
          'frames/cropped_frame20.png', 'frames/cropped_frame21.png', 'frames/cropped_frame22.png', 'frames/cropped_frame23.png', 
          'frames/cropped_frame24.png', 'frames/cropped_frame25.png', 'frames/cropped_frame26.png', 'frames/cropped_frame27.png', 
          'frames/cropped_frame28.png', 'frames/cropped_frame29.png', 'frames/cropped_frame30.png', 'frames/cropped_frame31.png', 
          'frames/cropped_frame32.png', 'frames/cropped_frame33.png', 'frames/cropped_frame34.png', 'frames/cropped_frame35.png', 
          'frames/cropped_frame36.png', 'frames/cropped_frame37.png', 'frames/cropped_frame38.png', 'frames/cropped_frame39.png', 
          'frames/cropped_frame40.png', 'frames/cropped_frame41.png', 'frames/cropped_frame42.png', 'frames/cropped_frame43.png', 
          'frames/cropped_frame44.png', 'frames/cropped_frame45.png', 'frames/cropped_frame46.png', 'frames/cropped_frame47.png', 
          'frames/cropped_frame48.png', 'frames/cropped_frame49.png', 'frames/cropped_frame50.png', 'frames/cropped_frame51.png', 
          'frames/cropped_frame52.png', 'frames/cropped_frame53.png', 'frames/cropped_frame54.png', 'frames/cropped_frame55.png', 
          'frames/cropped_frame56.png', 'frames/cropped_frame57.png', 'frames/cropped_frame58.png', 'frames/cropped_frame59.png', 
          'frames/cropped_frame60.png', 'frames/cropped_frame61.png', 'frames/cropped_frame62.png', 'frames/cropped_frame63.png', 
          'frames/cropped_frame64.png', 'frames/cropped_frame65.png', 'frames/cropped_frame66.png', 'frames/cropped_frame67.png', 
          'frames/cropped_frame68.png', 'frames/cropped_frame69.png', 'frames/cropped_frame70.png', 'frames/cropped_frame71.png', 
          'frames/cropped_frame72.png', 'frames/cropped_frame73.png', 'frames/cropped_frame74.png', 'frames/cropped_frame75.png', 
          'frames/cropped_frame76.png', 'frames/cropped_frame77.png', 'frames/cropped_frame78.png', 'frames/cropped_frame79.png', 
          'frames/cropped_frame80.png', 'frames/cropped_frame81.png', 'frames/cropped_frame82.png', 'frames/cropped_frame83.png', 
          'frames/cropped_frame84.png', 'frames/cropped_frame85.png', 'frames/cropped_frame86.png', 'frames/cropped_frame87.png', 
          'frames/cropped_frame88.png', 'frames/cropped_frame89.png', 'frames/cropped_frame90.png', 'frames/cropped_frame91.png', 
          'frames/cropped_frame92.png', 'frames/cropped_frame93.png', 'frames/cropped_frame94.png', 'frames/cropped_frame95.png', 
          'frames/cropped_frame96.png', 'frames/cropped_frame97.png', 'frames/cropped_frame98.png', 'frames/cropped_frame99.png', 
          'frames/cropped_frame100.png', 'frames/cropped_frame101.png', 'frames/cropped_frame102.png', 'frames/cropped_frame103.png', 
          'frames/cropped_frame104.png', 'frames/cropped_frame105.png', 'frames/cropped_frame106.png', 'frames/cropped_frame107.png', 
          'frames/cropped_frame108.png', 'frames/cropped_frame109.png', 'frames/cropped_frame110.png', 'frames/cropped_frame111.png', 
          'frames/cropped_frame112.png', 'frames/cropped_frame113.png', 'frames/cropped_frame114.png', 'frames/cropped_frame115.png']

#result, timestamps = get_slide_timestamps("test_videos/english_history.mp4", squashed_json)
# print(timestamps)
# if result:
#     print(timestamps)
# else:
#     print("slide timestamping did not work for english history")

timestamps = match_frames(transitions, frames, squashed_json)
print(timestamps)