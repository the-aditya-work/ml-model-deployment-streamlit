import streamlit as st
import numpy as np
import pickle

# Load model
with open("model/trained_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌸 Iris Flower Species Predictor")
st.markdown("Enter flower features to get prediction:")

# Inputs
sepal_length = st.slider('Sepal Length', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal Width', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width', 0.1, 2.5, 1.0)

# Prediction
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    
    species = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"Predicted Species: **{species[prediction]}**")
    
    st.subheader("Prediction Probabilities")
    st.bar_chart(probabilities)
