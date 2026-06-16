import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page Configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI FAQ Chatbot")

st.write(
    "Ask questions related to Artificial Intelligence, "
    "Machine Learning, Data Science, and related topics."
)

st.divider()

# Load FAQ Dataset
faq_data = pd.read_csv("faq_data.csv")

# Convert all FAQ questions to lowercase
faq_questions = [
    question.lower()
    for question in faq_data["Question"].tolist()
]

faq_answers = faq_data["Answer"].tolist()

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(faq_questions)

# User Input
user_question = st.text_input(
    "Ask Your Question",
    placeholder="Example: What is Machine Learning?"
).lower()

# Answer Button
if st.button("Get Answer"):

    if not user_question.strip():

        st.warning("Please enter a question.")

    else:

        # Convert user question into vector
        user_vector = vectorizer.transform([user_question])

        # Calculate similarity
        similarity_scores = cosine_similarity(
            user_vector,
            question_vectors
        )

        highest_score = similarity_scores.max()

        if highest_score < 0.50:

            st.error(
                "Sorry, I could not find a relevant answer for your question."
            )

        else:

            best_match_index = similarity_scores.argmax()

            chatbot_answer = faq_answers[best_match_index]

            st.subheader("Answer")

            st.success(chatbot_answer)

            st.caption(
                f"Confidence Score: {highest_score:.2f}"
            )

# Footer
st.divider()

st.caption(
    "Developed by Vishal Kumar | CodeAlpha Artificial Intelligence Internship"
)