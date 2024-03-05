from image_similarity import ImageComparator
from text_similarity import convert_to_text, get_ocr_similarity_score


class SlideComparator():
    def __init__(self):
        self.imageComparator = ImageComparator()

    def get_similarity_score(self, first_image_path, second_image_path):
        text1 = convert_to_text(first_image_path)
        text2 = convert_to_text(second_image_path)
        text_score = get_ocr_similarity_score(text1, text2)
        image_score = self.imageComparator.get_similarity_score(first_image_path, second_image_path)
        return text_score, image_score

    def is_similar(self, first_image_path, second_image_path, slide_slide_comp=True):
        if slide_slide_comp:
            TEXT_MATCH_PROB = 0.9
            TEXT_IGNORE_PROB = 0.01
            IMAGE_SAFE_MATCH_PROB = 0.91
            IMAGE_MATCH_PROB = 0.945
        else:
            TEXT_MATCH_PROB = 0.8
            TEXT_IGNORE_PROB = 0.01
            IMAGE_SAFE_MATCH_PROB = 0.85
            IMAGE_MATCH_PROB = 0.9

        text_score, image_score = self.get_similarity_score(first_image_path, second_image_path)

        return text_score > TEXT_MATCH_PROB or (
                text_score < TEXT_IGNORE_PROB and image_score > IMAGE_SAFE_MATCH_PROB) or image_score > IMAGE_MATCH_PROB


if __name__ == "__main__":
    # shouldMatch = True
    slideComparator = SlideComparator()
    image1 = 'frames/cropped_frame213.png'
    image2 = 'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-45.png'
    text_score, image_score, result = slideComparator.get_similarity_score(image1, image2)
    print(result)
    # with open("slide_similarities.csv", "a") as f:
    #     # f.write(f"{TEXT_MATCH_PROB},{TEXT_IGNORE_PROB},{IMAGE_SAFE_MATCH_PROB},{IMAGE_MATCH_PROB},{image1},{image2},{text_score},{image_score},{result},{shouldMatch}\n")
