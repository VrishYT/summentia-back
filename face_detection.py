import cv2
import numpy as np

class FaceDetector():
    def __init__(self):
        self.face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def detect_bounding_box(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray_frame, scaleFactor = 1.1, minNeighbors = 15, minSize=(50, 50))
        return faces

    def detect_face(self, video):
        vidObj = cv2.VideoCapture(video)
        fps = vidObj.get(cv2.CAP_PROP_FPS)
        curr_frame = 0
        boxes = []
        while True:
            success, video_frame = vidObj.read()
            if not success:
                break
            
            bounding_box = self.detect_bounding_box(video_frame)
            if curr_frame == 0:
                boxes = bounding_box
            elif len(bounding_box) != 0:
                boxes = np.concatenate((boxes, bounding_box), axis=0)
                
            curr_frame += fps
            vidObj.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
                
        return boxes

if __name__ == "__main__":
    face_detector = FaceDetector()
    
    bounding_boxes = face_detector.detect_face("./video.mp4")
    
    print(bounding_boxes[0].shape)
    
