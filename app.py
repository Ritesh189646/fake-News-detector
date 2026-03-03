import streamlit as st
import joblib

# Required for loading pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load trained model
model = joblib.load("fake_news_model.pkl")

st.title("📰 Fake News Detection App")
st.write("Paste a news headline or short news text below:")

user_text = st.text_area("News Text")

if st.button("Check"):
    if user_text.strip() == "":
        st.warning("Please enter some text")
    else:
        prediction = model.predict([user_text])[0]
        probability = model.predict_proba([user_text])[0]

        fake_prob = probability[0] * 100
        real_prob = probability[1] * 100

        if prediction == 0:
            st.error(f"❌ This news is FAKE\n\nConfidence: {fake_prob:.2f}%")
        else:
            st.success(f"✅ This news is REAL\n\nConfidence: {real_prob:.2f}%")
