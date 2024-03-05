import cv2
import pytesseract
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def convert_to_text(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

def get_ocr_similarity_score(text1, text2):
    # If both texts are whitespace then return a score 0
    if text1.isspace() and text2.isspace():
        return 0
    
    # Convert the texts into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    
    if text1 == text2:
        return 1
    
    vectors = vectorizer.fit_transform([text1, text2])
    # Calculate the cosine similarity between the vectors
    similarity = cosine_similarity(vectors)
    return similarity[0,1]    

