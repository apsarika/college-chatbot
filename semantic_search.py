import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Clean text for better matching
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

# Load and preprocess data
with open("data.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)
    paragraphs = [clean_text(item["content"]) for item in raw_data]

# Initialize TF-IDF
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(paragraphs)

# Function to find the best matching paragraph
def get_best_match(query):
    query = clean_text(query)
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, vectors)

    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    if best_score < 0.05:
        return "Sorry, I couldn't find a good answer to your question."

    return raw_data[best_match_index]["content"]

