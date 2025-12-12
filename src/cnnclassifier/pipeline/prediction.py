import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts/training", "model.h5"))

       
        img = image.load_img(self.filename, target_size=(224, 224))
        img = image.img_to_array(img)
        img = img / 255.0      
        img = np.expand_dims(img, axis=0)

        preds = model.predict(img)
        result = np.argmax(preds, axis=1)[0]


        class_names = ["Normal", "Tumor"]

        Prediction = class_names[result]

        return [{'image': Prediction}]
