# 🧠 Fake News Detector

A machine learning-powered web app that classifies news headlines as **REAL** or **FAKE**—built using Python, scikit-learn, and Streamlit.

## 🚀 Live Demo
*(Optional: Add deployment link here if you publish it)*

## 🎯 Features
- Paste any news headline and get an instant prediction
- Confidence score included for model transparency
- Sample headline buttons for quick testing
- Clean, mobile-friendly Streamlit UI

## 🧪 Tech Stack
- Python 3
- scikit-learn
- pandas
- Streamlit
- joblib (for saving/loading models)

## 🛠 How It Works
1. Trained on combined real and fake news datasets (`Fake.csv`, `True.csv`)
2. Vectorized using `TfidfVectorizer`
3. Classification using `LogisticRegression`
4. Frontend built entirely in Streamlit

## 📁 File Structure
