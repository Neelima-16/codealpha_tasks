import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Dataset
faq_data = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! How can I assist you?",
    "how are you": "I'm doing great. Thanks for asking!",
    "what is python": "Python is a high-level programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI that enables systems to learn from data.",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "what is data science": "Data Science is the field of extracting insights from data.",
    "what is a chatbot": "A chatbot is a program that simulates human conversation.",
    "what is cloud computing": "Cloud computing provides computing services over the internet.",
    "what is a database": "A database is an organized collection of data.",
    "what is sql": "SQL is a language used to manage databases.",
    "what is git": "Git is a version control system.",
    "what is github": "GitHub is a platform for hosting and collaborating on Git repositories.",
    "thank you": "You're welcome! Happy to help."
}

# Prepare NLP Data
questions = list(faq_data.keys())

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(questions)

# Page Configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI
st.title("🤖 FAQ Chatbot")

st.write(
    "Ask a question and I'll try to find the best answer from my FAQ database."
)

user_question = st.text_input("Enter your question")

get_answer = st.button("Get Answer")

# Chatbot Logic
if get_answer:

    question = user_question.lower().strip()

    if question:

        user_vector = vectorizer.transform([question])

        similarity_scores = cosine_similarity(
            user_vector,
            faq_vectors
        )

        best_match_index = similarity_scores.argmax()

        best_score = similarity_scores[0][best_match_index]

        if best_score > 0.2:

            best_question = questions[best_match_index]

            answer = faq_data[best_question]

            st.session_state.chat_history.append(
                ("You", user_question)
            )

            st.session_state.chat_history.append(
                ("Bot", answer)
            )

            st.markdown("### 🤖 Bot Response")
            st.info(answer)

        else:

            st.markdown("### 🤖 Bot Response")
            st.warning(
                "Sorry, I couldn't find a suitable answer."
            )

# Display Chat History
if st.session_state.chat_history:

    st.markdown("## 💬 Chat History")

    for sender, message in st.session_state.chat_history:

        if sender == "You":
            st.markdown(f"**🧑 You:** {message}")

        else:
            st.markdown(f"**🤖 Bot:** {message}")