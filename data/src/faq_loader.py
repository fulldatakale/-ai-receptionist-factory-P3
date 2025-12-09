import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQRetriever:
    def __init__(self, faq_path: str):
        self.df = pd.read_csv(faq_path)
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(self.df["question"])

    def retrieve(self, query: str, top_k: int = 3):
        q_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(q_vec, self.matrix)[0]
        indices = scores.argsort()[::-1][:top_k]
        results = []
        for idx in indices:
            results.append({
                "question": self.df.iloc[idx]["question"],
                "answer": self.df.iloc[idx]["answer"],
                "score": float(scores[idx]),
            })
        return results
