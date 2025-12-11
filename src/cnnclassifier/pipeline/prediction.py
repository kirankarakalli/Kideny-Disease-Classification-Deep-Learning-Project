import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("artifacts/training", "model.h5"))

        # Load and preprocess image
        img = image.load_img(self.filename, target_size=(224, 224))
        img = image.img_to_array(img)
        img = img / 255.0      # VERY IMPORTANT
        img = np.expand_dims(img, axis=0)

        # Prediction
        preds = model.predict(img)
        result = np.argmax(preds, axis=1)[0]

        # result = 0 or 1
        # YOU MUST CONFIRM THIS MAPPING FROM training.class_indices

        class_names = ["Normal", "Tumor"]

        Prediction = class_names[result]

        return [{'image': Prediction}]
