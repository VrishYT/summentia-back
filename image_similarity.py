import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from keras.applications.vgg16 import VGG16
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.preprocessing import image


class ImageComparator():
    def __init__(self):
        self._vgg16 = VGG16(weights='imagenet', include_top=False,
                            pooling='max', input_shape=(1000, 1000, 3))

        for model_layer in self._vgg16.layers:
            model_layer.trainable = False

    # Load the image provided
    def _load_image(self, image_path):
        input_image = Image.open(image_path)
        rgb_image = input_image.convert("RGB")
        resized_image = rgb_image.resize((1000, 1000))

        return resized_image

    # Convert image into 3D array and add additional dimension for model input
    def _get_image_embeddings(self, object_image):
        image_array = np.expand_dims(image.img_to_array(object_image), axis=0)
        image_embedding = self._vgg16.predict(image_array)

        return image_embedding

    def show_image(aelf, image_path):
        image = mpimg.imread(image_path)
        imgplot = plt.imshow(image)
        plt.show()

    # Takes image array and computes its embedding using VGG16 model
    def get_similarity_score(self, first_image_path, second_image_path):
        first_image = self._load_image(first_image_path)
        second_image = self._load_image(second_image_path)

        first_image_vector = self._get_image_embeddings(first_image)
        second_image_vector = self._get_image_embeddings(second_image)

        similarity_score = cosine_similarity(first_image_vector,
                                             second_image_vector).reshape(1, )

        return similarity_score[0]
