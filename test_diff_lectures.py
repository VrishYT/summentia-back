from slide_squashing import squash_slides
from split_pdf import convert_pdf_to_png
from slide_timestamping import get_slide_timestamps
#convert_pdf_to_png("test_slide_pdfs/intro_to_psychology.pdf", "test_slides/intro_to_psychology/output_image")
# gradient_slides_json = {
#         "num_slides": 12,
#         "slides": [
#             "test_slides/gradient_descent/output_image_page_1.png",
#             "test_slides/gradient_descent/output_image_page_2.png",
#             "test_slides/gradient_descent/output_image_page_3.png",
#             "test_slides/gradient_descent/output_image_page_4.png",
#             "test_slides/gradient_descent/output_image_page_5.png",
#             "test_slides/gradient_descent/output_image_page_6.png",
#             "test_slides/gradient_descent/output_image_page_7.png",
#             "test_slides/gradient_descent/output_image_page_8.png",
#             "test_slides/gradient_descent/output_image_page_9.png",
#             "test_slides/gradient_descent/output_image_page_10.png",
#             "test_slides/gradient_descent/output_image_page_11.png",
#             "test_slides/gradient_descent/output_image_page_12.png"
#         ]
#     }

psychology_slides_json = {
        "num_slides": 18,
        "slides": [
            "test_slides/intro_to_psychology/output_image_page_1.png",
            "test_slides/intro_to_psychology/output_image_page_2.png",
            "test_slides/intro_to_psychology/output_image_page_3.png",
            "test_slides/intro_to_psychology/output_image_page_4.png",
            "test_slides/intro_to_psychology/output_image_page_5.png",
            "test_slides/intro_to_psychology/output_image_page_6.png",
            "test_slides/intro_to_psychology/output_image_page_7.png",
            "test_slides/intro_to_psychology/output_image_page_8.png",
            "test_slides/intro_to_psychology/output_image_page_9.png",
            "test_slides/intro_to_psychology/output_image_page_10.png",
            "test_slides/intro_to_psychology/output_image_page_11.png",
            "test_slides/intro_to_psychology/output_image_page_12.png",
            "test_slides/intro_to_psychology/output_image_page_13.png",
            "test_slides/intro_to_psychology/output_image_page_14.png",
            "test_slides/intro_to_psychology/output_image_page_15.png",
            "test_slides/intro_to_psychology/output_image_page_16.png",
            "test_slides/intro_to_psychology/output_image_page_17.png",
            "test_slides/intro_to_psychology/output_image_page_18.png"
        ]
    }


squashed_json = squash_slides(psychology_slides_json)
print(f"squashed slides: {squashed_json}")
result, timestamps = get_slide_timestamps("test_videos/intro_to_psychology.mp4", squashed_json)
if result:
    print(timestamps)
else:
    print("slide timestamping did not work for gradient descent")
