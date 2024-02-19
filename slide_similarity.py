from image_similarity import ImageComparator
from text_similarity import convert_to_text, get_ocr_similarity_score

TEXT_MATCH_PROB = 0.9
TEXT_IGNORE_PROB = 0.01
IMAGE_SAFE_MATCH_PROB = 0.91
IMAGE_MATCH_PROB = 0.945

class SlideComparator():
    def __init__(self):
        self.imageComparator = ImageComparator()

    def get_similarity_score(self, first_image_path, second_image_path):
        text1 = convert_to_text(first_image_path)
        text2 =  convert_to_text(second_image_path)
        text_score = get_ocr_similarity_score(text1, text2)
        image_score = self.imageComparator.get_similarity_score(first_image_path, second_image_path)
        print(f"text score: {text_score}")
        print (f"image score: {image_score}")
        return self.is_similar(text_score, image_score)
    
    def is_similar(self, text_score, image_score):
        return text_score > TEXT_MATCH_PROB  or (text_score < TEXT_IGNORE_PROB and image_score > IMAGE_SAFE_MATCH_PROB) or image_score > IMAGE_MATCH_PROB
            
    def can_squash(self, text_score, image_score):
        return False



slideComparator = SlideComparator()
# result = slideComparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-40.png', 'frames/cropped_frame166.png')
result = slideComparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-41.png', 'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-40.png')
print(result)