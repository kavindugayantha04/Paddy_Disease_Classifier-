import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# 1. Load Model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('paddy_model2.keras')
    return model

model = load_model()

class_names = [
    'bacterial_leaf_blight', 'bacterial_leaf_streak', 'bacterial_panicle_blight', 
    'blast', 'brown_spot', 'dead_heart', 'downy_mildew', 
    'hispa', 'normal', 'tungro'
]

st.title("🌾 Paddy Disease Classifier")

file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if file is not None:
    # 1. Open and convert to RGB (Standardize channels)
    image = Image.open(file).convert("RGB")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption='Original Upload', use_column_width=True)

    # --- MATCHING THE TRAINING PIPELINE ---
    
    
    target_size = (128, 128) 
    image = image.resize(target_size) 
    
    img_array = np.asarray(image).astype(np.float32)
    
   
    
    # Add batch dimension (1, 128, 128, 3)
    img_reshape = np.expand_dims(img_array, axis=0)

    
    st.write(f"🔍 Debug Info: Input Max Value: {np.max(img_array)} (Should be ~255)")

    if st.button("Predict"):
        prediction = model.predict(img_reshape)
        
       
        probabilities = prediction[0]
        
        predicted_class_index = np.argmax(probabilities)
        predicted_class = class_names[predicted_class_index]
        confidence = probabilities[predicted_class_index] * 100
        
        with col2:
            st.success(f"Prediction: **{predicted_class}**")
            st.info(f"Confidence: {confidence:.2f}%")
            
            # Show bar chart of all probabilities to see if model is confused
            st.bar_chart(dict(zip(class_names, probabilities)))