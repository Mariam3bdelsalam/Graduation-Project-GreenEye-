# 🌱 Plant Disease Classification Model

This module is part of **Green Eye**, an AI-powered agriculture application that helps farmers identify plant diseases from leaf images.

## 📌 Overview

The Plant Disease Model is a deep learning image classification model that predicts the **disease class of a plant** based on an uploaded leaf image.

The model was trained using the **Plant Disease Classification Merged Dataset** from Kaggle, which contains images of healthy and diseased plants across multiple crops and disease categories.

**Dataset:**
Plant Disease Classification Merged Dataset
https://www.kaggle.com/datasets/alinedobrovsky/plant-disease-classification-merged-dataset

## 📊 Dataset

* **Images:** ~79,000
* **Classes:** 88
* **Image Type:** RGB images
* **Task:** Multi-class image classification
* **Classes:** Healthy and diseased plant leaves
* **Multiple crop species and disease types**

The dataset combines multiple plant disease datasets to provide a larger and more diverse training set.

## 🧠 Model

The model uses **DenseNet121** with Transfer Learning.

### Training approach

1. Load the pre-trained DenseNet121 model.
2. Replace the original classification head with a custom classification layer.
3. Train the classification head on the plant disease dataset.
4. Apply data augmentation to improve generalization.
5. Fine-tune selected layers of the pre-trained model.
6. Evaluate the model on the validation dataset.

### Techniques Used

* Transfer Learning
* Data Augmentation
* Fine-Tuning
* GPU Training

## 🖼️ Input

The model receives an image of a plant leaf.

Example:

```text
Leaf Image
    ↓
Image Preprocessing
    ↓
DenseNet121
    ↓
Disease Classification
```

## 🎯 Output

The model returns the predicted disease class.

Example:

```json
{
  "prediction": "Tomato___Late_blight",
  "confidence": 0.94
}
```

## 🚀 Use in Green Eye

The Plant Disease Model is integrated into the **Green Eye** application.

The user can upload or capture an image of a plant leaf, and the model predicts the corresponding disease.

```text
User
  ↓
Upload Plant Image
  ↓
Green Eye
  ↓
Plant Disease Model
  ↓
Predicted Disease
  ↓
Disease Information / Recommendation
```

## 🛠️ Technologies

* Python
* TensorFlow / Keras
* DenseNet121
* NumPy
* OpenCV
* Kaggle GPU

## 📈 Model Evaluation

The model is evaluated using:

* Accuracy
* Confusion Matrix

## 📁 Project Structure

```text
plant-disease/
│
├── training/
│   └── plant_disease_training.ipynb
│
├── model/
│   └── plant_disease_model.h5
│
├── class_names.json
│
├── inference.py
│
└── README.md
```

## ⚠️ Disclaimer

This model is intended to assist with **plant disease identification** and should not be considered a replacement for professional agricultural diagnosis.

## 📚 Dataset Citation

Dobrovsky, A. (2024). *Plant Disease Classification Merged Dataset*. Kaggle.

Dataset license and attribution requirements should be checked before redistribution or commercial use.
