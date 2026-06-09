# FAQ Chatbot

## Overview

This project is a FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.

The chatbot uses Natural Language Processing (NLP) techniques to understand user questions and provide the most relevant answer from a predefined FAQ database. It uses TF-IDF Vectorization and Cosine Similarity to match user queries with stored FAQs.

## Features

* Interactive chatbot interface using Streamlit
* NLP-based question matching
* TF-IDF Vectorization
* Cosine Similarity for finding relevant answers
* Maintains chat history during the session
* Handles different variations of user questions
* User-friendly interface

## Technologies Used

* Python
* Streamlit
* NLTK
* Scikit-learn

## NLP Techniques Used

### TF-IDF Vectorization

Converts FAQ questions and user queries into numerical vectors.

### Cosine Similarity

Calculates the similarity between the user query and stored FAQ questions to find the most relevant answer.

## Installation

### 1. Clone the Repository

```bash
git clone <repository_link>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

## Project Structure

```text
CodeAlpha_FAQ_Chatbot
│
├── app.py
├── requirements.txt
└── README.md
```

## Sample Questions

* What is Python?
* Tell me about Python
* What is AI?
* Explain AI
* What do you know about GitHub?
* What is NLP?
* What is Machine Learning?

## Future Enhancements

* Voice-based chatbot interaction
* Larger FAQ knowledge base
* Integration with databases
* Support for multiple languages
* AI-powered conversational responses

## Author

Neelima Kakulapati

## Internship

CodeAlpha Artificial Intelligence Internship Project
