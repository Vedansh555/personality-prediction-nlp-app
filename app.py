# Paste your full Streamlit code here 👇

import streamlit as st
import joblib
import matplotlib.pyplot as plt

# Load model + vectorizer
model = joblib.load("multi_rf.pkl")
tfidf = joblib.load("tfidf.pkl")
traits = ['cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN']

def plot_traits(pred):
    colors = ['green' if v == 1 else 'red' for v in pred]
    plt.barh(traits, pred, color=colors)
    plt.xlim(0, 1.2)
    plt.xlabel("Prediction")
    plt.title("Personality Traits")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    st.pyplot(plt)

st.title("🧠 Personality Predictor")
text = st.text_area("Paste your text:")

if st.button("Predict"):
    if text.strip():
        vec = tfidf.transform([text])
        pred = model.predict(vec)[0].tolist()
        st.subheader("Prediction Results:")
        for trait, val in zip(traits, pred):
            st.write(f"**{trait}**: {'✅ Present' if val else '❌ Absent'}")
        plot_traits(pred)
    else:
        st.warning("Please enter some text.")
