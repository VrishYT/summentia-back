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

# english_history_json = {
#         "num_slides": 45,
#         "slides": [
#             "test_slides/english_history/output_image_page_1.png",
#             "test_slides/english_history/output_image_page_2.png",
#             "test_slides/english_history/output_image_page_3.png",
#             "test_slides/english_history/output_image_page_4.png",
#             "test_slides/english_history/output_image_page_5.png",
#             "test_slides/english_history/output_image_page_6.png",
#             "test_slides/english_history/output_image_page_7.png",
#             "test_slides/english_history/output_image_page_8.png",
#             "test_slides/english_history/output_image_page_9.png",
#             "test_slides/english_history/output_image_page_10.png",
#             "test_slides/english_history/output_image_page_11.png",
#             "test_slides/english_history/output_image_page_12.png",
#             "test_slides/english_history/output_image_page_13.png",
#             "test_slides/english_history/output_image_page_14.png",
#             "test_slides/english_history/output_image_page_15.png",
#             "test_slides/english_history/output_image_page_16.png",
#             "test_slides/english_history/output_image_page_17.png",
#             "test_slides/english_history/output_image_page_18.png",
#             "test_slides/english_history/output_image_page_19.png",
#             "test_slides/english_history/output_image_page_20.png",
#             "test_slides/english_history/output_image_page_21.png",
#             "test_slides/english_history/output_image_page_22.png",
#             "test_slides/english_history/output_image_page_23.png",
#             "test_slides/english_history/output_image_page_24.png",
#             "test_slides/english_history/output_image_page_25.png",
#             "test_slides/english_history/output_image_page_26.png",
#             "test_slides/english_history/output_image_page_27.png",
#             "test_slides/english_history/output_image_page_28.png",
#             "test_slides/english_history/output_image_page_29.png",
#             "test_slides/english_history/output_image_page_30.png",
#             "test_slides/english_history/output_image_page_31.png",
#             "test_slides/english_history/output_image_page_32.png",
#             "test_slides/english_history/output_image_page_33.png",
#             "test_slides/english_history/output_image_page_34.png",
#             "test_slides/english_history/output_image_page_35.png",
#             "test_slides/english_history/output_image_page_36.png",
#             "test_slides/english_history/output_image_page_37.png",
#             "test_slides/english_history/output_image_page_38.png",
#             "test_slides/english_history/output_image_page_39.png",
#             "test_slides/english_history/output_image_page_40.png",
#             "test_slides/english_history/output_image_page_41.png",
#             "test_slides/english_history/output_image_page_42.png",
#             "test_slides/english_history/output_image_page_43.png",
#             "test_slides/english_history/output_image_page_44.png",
#             "test_slides/english_history/output_image_page_45.png",
#         ]
#     }


result, timestamps = get_slide_timestamps("test_videos/gradient_descent.mp4", slides_info, "./")
print(timestamps)
if result:
    print(timestamps)
else:
    print("slide timestamping did not work for gradient descent")

# timestamps = match_frames(transitions, frames, squashed_json)
# print(timestamps)