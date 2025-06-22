# personality-prediction-nlp-app
# 🧠 Personality Prediction from Text using Machine Learning

This project is a **Streamlit web app** that predicts the **Big Five Personality Traits** (OCEAN model) — based on user-submitted essays or paragraphs — using Natural Language Processing and a trained Machine Learning model.

### 🚀 Try the Live App:
👉 [Click here to open the app](https://your-username-your-repo-name.streamlit.app)  
> _(Replace with your actual Streamlit link)_

---

## 📌 About the Project

This project uses:
- ✅ **Text classification** techniques
- ✅ **TF-IDF vectorization** for text representation
- ✅ **Multi-output Random Forest** classifier
- ✅ **Streamlit** for the front-end user interface

Given any piece of writing (like an essay, post, or journal entry), it predicts if each of the following **5 traits** is present:

| Trait        | Meaning                         |
|--------------|----------------------------------|
| **cEXT**     | Extraversion                    |
| **cNEU**     | Neuroticism                     |
| **cAGR**     | Agreeableness                   |
| **cCON**     | Conscientiousness              |
| **cOPN**     | Openness to Experience          |

---

## 🧠 Model Training Details

- 📁 Dataset: MyPersonality Project (preprocessed subset)
- 🔡 Text Preprocessing: Cleaning, lowercasing, stopwords removal
- 📊 Vectorization: `TfidfVectorizer()`
- 🤖 Model: `RandomForestClassifier()` using `MultiOutputClassifier`
- 📈 Accuracy: Varies per trait (~70–80% for balanced traits)

---

## 🛠️ Tech Stack

| Component    | Tool/Library       |
|--------------|--------------------|
| ML Model     | Scikit-learn       |
| NLP          | NLTK + TF-IDF      |
| Frontend     | Streamlit          |
| Visualization| Matplotlib         |
| Deployment   | Streamlit Cloud    |

---

## 💻 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/personality-predictor.git
   cd personality-predictor
