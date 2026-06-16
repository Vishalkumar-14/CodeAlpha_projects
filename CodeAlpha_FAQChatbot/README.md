# 🤖 AI FAQ Chatbot

This project was developed as part of the CodeAlpha Artificial Intelligence Internship Program.

The AI FAQ Chatbot is a simple NLP-based application that answers user questions related to Artificial Intelligence, Machine Learning, Data Science, and other related topics. The chatbot uses Natural Language Processing techniques to identify the most relevant question from a predefined FAQ database and returns the corresponding answer.

The main objective of this project was to understand how information retrieval systems work and how NLP techniques can be used to build intelligent question-answering applications.

---

## Features

* Interactive chatbot interface built with Streamlit
* Answers frequently asked questions related to AI and Machine Learning
* Uses TF-IDF Vectorization for text representation
* Uses Cosine Similarity for question matching
* Confidence score for answer relevance
* Handles unknown questions using a confidence threshold
* Simple and user-friendly interface

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## Project Structure

```text
CodeAlpha_FAQChatbot/
│
├── app.py
├── faq_data.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How It Works

1. The FAQ dataset is loaded from a CSV file.
2. All FAQ questions are converted into numerical vectors using TF-IDF Vectorization.
3. When a user enters a question, it is converted into a vector using the same TF-IDF model.
4. Cosine Similarity is used to compare the user question with all stored FAQ questions.
5. The most relevant answer is returned if the similarity score exceeds the confidence threshold.
6. If no suitable match is found, the chatbot displays a friendly message indicating that no relevant answer is available.

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Example Questions

* What is Artificial Intelligence?
* What is Machine Learning?
* What is Deep Learning?
* What is NLP?
* What is TensorFlow?
* What is Generative AI?

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing (NLP)
* Text preprocessing
* TF-IDF Vectorization
* Cosine Similarity
* Building interactive applications using Streamlit
* Working with structured datasets

---

## Future Improvements

* Chat history support
* Larger knowledge base
* Integration with LLM APIs such as Gemini or OpenAI
* Voice-based interaction
* Multi-domain FAQ support

---

## Author

**Vishal Kumar**

B.Tech CSE (AI & ML)
Graphic Era Deemed to be University

Project completed as part of the **CodeAlpha Artificial Intelligence Internship Program**.
