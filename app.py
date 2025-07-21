import streamlit as st
import joblib

# 🎯 Load model and vectorizer
model = joblib.load("model (2).pkl")
vectorizer = joblib.load("vectorizer (2).pkl")

# ⚙️ Configure page
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto"
)

# 🔥 Hero Section (Header)
st.markdown("""
    <style>
    .main-title {
        font-size: 48px;
        text-align: center;
        color: #1f77b4;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .tagline {
        font-size: 20px;
        text-align: center;
        color: #333;
        margin-bottom: 50px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #aaa;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🧠 Fake News Detector</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Empowering readers to separate truth from misinformation — instantly.</div>", unsafe_allow_html=True)

# 🧪 Main Layout with Columns
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("📋 How It Works")
    st.write("""
    This tool uses a machine learning model trained on thousands of real and fake news headlines.  
    Paste any headline and discover whether it’s:
    - ✅ Real News — credible and factual  
    - ❌ Fake News — likely misleading or fabricated  
    You’ll also see a confidence score that reflects how sure the model is.
    """)

    st.markdown("📌 **Try one of these examples:**")
    examples = [
        "NASA confirms discovery of water on Mars",
        "Aliens spotted building pyramids in Antarctica",
        "Chocolate cures COVID in 24 hours"
    ]
    for ex in examples:
        if st.button(ex):
            st.session_state.headline = ex

with col2:
    st.subheader("🔍 Enter a News Headline")
    user_input = st.text_area("✍️ Headline", value=st.session_state.get("headline", ""), placeholder="Type or paste a headline here...")

    if st.button("🚀 Detect"):
        if user_input.strip():
            input_vector = vectorizer.transform([user_input])
            prediction = model.predict(input_vector)[0]
            prob = model.predict_proba(input_vector)[0]
            confidence = round(max(prob) * 100, 2)

            result = "❌ FAKE NEWS" if prediction == 1 else "✅ REAL NEWS"
            st.success(f"**Prediction:** {result}")
            st.info(f"Confidence Score: {confidence}%")
        else:
            st.warning("Please enter a headline.")

# 🏁 Footer
st.markdown("<div class='footer'>Made with 💙 by Sahithi · Powered by Streamlit & Scikit-learn · © 2025</div>", unsafe_allow_html=True)