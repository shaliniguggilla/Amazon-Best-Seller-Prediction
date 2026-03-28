import streamlit as st
import pickle
import numpy as np

st.title("📚 Bestseller Prediction App")

# Load model
with open("bestseller_model.pkl", "rb") as file:
    model = pickle.load(file)

# Inputs
reviews = st.number_input("Enter Reviews")
price = st.number_input("Enter Price")
genre = st.selectbox("Genre", ["Fiction", "Non Fiction"])

# Convert genre
genre_val = 0 if genre == "Fiction" else 1

# Predict
if st.button("Predict"):
    input_data = np.array([[reviews, price, genre_val]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Bestseller")
    else:
        st.error("❌ Not a Bestseller")