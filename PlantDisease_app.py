from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import tensorflow as tf
import json

app = FastAPI(title="Plant Disease Detection API")

# Load model
model = tf.keras.models.load_model("model2.keras")

# Load class names
with open("class_names.json", "r") as f:
    class_names = json.load(f)

# Load disease info
with open("disease_info.json", "r") as f:
    disease_info = json.load(f)

IMG_SIZE = 224

def preprocess_image(image: Image.Image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    image = preprocess_image(image)

    preds = model.predict(image)[0]
    class_index = np.argmax(preds)
    confidence = float(preds[class_index])

    class_name = class_names[class_index]
    info = disease_info.get(class_name, {})

    return {
        "class": class_name,
        "confidence": round(confidence * 100, 2),
        "cause": info.get("cause", "Not available"),
        "treatment": info.get("treatment", "Not available")
    }
