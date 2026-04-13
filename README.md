# 🌾 Paddy Disease Classifier

A deep learning-based web application for detecting paddy (rice) leaf diseases using a Convolutional Neural Network (CNN). This project uses a trained `.keras` model and provides predictions through a simple and interactive Streamlit interface.

---

## 📌 Project Overview

This system allows users to upload an image of a paddy leaf and get predictions about possible diseases.
It was developed as part of a learning process in deep learning and computer vision, combining theoretical knowledge with practical implementation.

---

## 🚀 Features

* 📸 Upload paddy leaf images
* 🤖 Predict disease using trained CNN model
* ⚡ Fast and simple Streamlit interface
* 🧠 Built using deep learning (TensorFlow/Keras)

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Framework:** Streamlit
* **Deep Learning:** TensorFlow / Keras
* **Libraries:** NumPy, OpenCV, PIL

---

## 📁 Project Structure

```
Paddy_Disease_Classifier-
│
├── app.py                  # Streamlit application
├── paddy_model2.keras      # Trained CNN model
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
└── notebooks/              # Training and experimentation
    ├── CnnModel.ipynb
    ├── cnn2.ipynb
    └── cnn3.ipynb
```

---

## 🧠 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Framework: TensorFlow / Keras
* Purpose: Image classification of paddy leaf diseases

The final trained model is stored as:

```
paddy_model2.keras
```

---

## 📂 Dataset

This project uses the **Paddy Doctor Dataset** for training the deep learning model.

👉 Dataset link:
https://www.kaggle.com/datasets/dasa7753912/new-paddy-doctor-paddy-disease-classification

### 📊 Dataset Details

* Contains images of paddy (rice) leaves
* Includes multiple disease classes and healthy samples
* Collected from real agricultural environments
* Suitable for CNN-based image classification

---

## 📊 Notebooks

The `notebooks/` folder contains Jupyter notebooks used during the learning and development process:

* CNN basics and experimentation
* Data preprocessing and augmentation
* Model training and evaluation

These notebooks were created before building the final classifier and helped in understanding deep learning concepts.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/kavindugayantha04/Paddy_Disease_Classifier-.git
cd Paddy_Disease_Classifier-
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

### 4. Open in browser

```
http://localhost:8501
```

---

## 📷 How It Works

1. User uploads a paddy leaf image
2. Image is preprocessed
3. Model predicts the disease class
4. Result is displayed on the UI

---

## 🎯 Purpose of the Project

* To learn and apply **Convolutional Neural Networks (CNNs)**
* To build a **real-world machine learning application**
* To gain experience with **model deployment using Streamlit**

---

## ⚠️ Notes

* The model file (`.keras`) is required to run the application
* Make sure it is placed in the root directory of the project
* Notebooks are included for learning and experimentation purposes

---

## 🙌 Acknowledgements

This project uses the **Paddy Doctor Dataset** available on Kaggle.
Special thanks to the dataset creators for providing high-quality data for research and learning.

---

## 📬 Contact

**Kavindu Gayantha**
GitHub: https://github.com/kavindugayantha04

---
