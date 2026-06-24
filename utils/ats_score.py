from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, jd_text):

    cv = CountVectorizer()

    matrix = cv.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(matrix)[0][1]

    return round(similarity * 100, 2)