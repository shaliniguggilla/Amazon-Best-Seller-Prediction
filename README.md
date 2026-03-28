📚 Bestseller Prediction & Recommendation System

🚀 Project Overview

This project aims to analyze bestselling books data and build a Machine Learning model to:

Predict whether a book will become a bestseller

Recommend similar books based on features

Generate meaningful business insights

🎯 Objectives

Perform Exploratory Data Analysis (EDA)

Build a prediction model using Machine Learning

Develop a recommendation system

Visualize key patterns in data

📂 Dataset

Dataset: Bestsellers with Categories

Features include:

Book Name

Author

User Rating

Reviews

Price

Genre

🧠 Workflow

Data Loading

Data Cleaning

Exploratory Data Analysis (EDA)

Feature Engineering

Model Building (Random Forest)

Model Evaluation

Recommendation System

Deployment using Streamlit

📊 Visualizations

Genre distribution

Rating distribution

Top authors

Price vs Rating

Correlation heatmap

🤖 Machine Learning Model

Algorithm: Random Forest Classifier

Target: Bestseller (0 or 1)

Features: Reviews, Price, Genre

💡 Key Insights

Higher reviews strongly influence bestseller success

Ratings play a major role in popularity

Certain authors dominate bestseller lists

Price has minimal impact

🔁 Recommendation System

Built using cosine similarity

Suggests similar books based on features

💾 Model Saving

Model saved using pickle:

bestseller_model.pkl

🌐 Deployment

Built using Streamlit

Users can input:

Reviews

Price

Genre

App predicts bestseller probability

Run app:

streamlit run app.py

🛠️ Tech Stack

Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

Streamlit

📌 How to Run

pip install -r requirements.txt

streamlit run app.py

📈 Future Improvements

Add NLP-based recommendation system

Deploy on cloud (AWS / Render)

Improve model accuracy

Add interactive dashboard

👩‍💻 Author

Deepika / Shalini
