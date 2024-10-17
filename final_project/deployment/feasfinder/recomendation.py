import re
import demoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


from contextlib import redirect_stdout
import os


with redirect_stdout(open(os.devnull, "w")):
    nltk.download('stopwords')

with redirect_stdout(open(os.devnull, "w")):
    nltk.download('wordnet')

with redirect_stdout(open(os.devnull, "w")):
    nltk.download('punkt')


# Text preprocssing
def clean_text(text):
    # Lowercasing
    text = text.lower()

    # Penghapusan Mention
    text = re.sub(r'@[A-Za-z0-9]+', '', text)

    # Penghapusan Hashtag
    text = re.sub(r'#', '', text)

    # Penghapusan Emoji
    text = demoji.replace(text, "")

    # Penghapusan Karakter Newline
    text = text.replace('\n', ' ')

    # Penghapusan Angka
    text = re.sub(r'\d+', '', text)

    # Penghapusan White Space Tambahan
    text = re.sub(r'\s+', ' ', text)

    # Pembersihan Teks Tambahan
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenisasi
    tokens = word_tokenize(text)

    # Pembersihan Teks
    tokens = [word for word in tokens if word.isalnum()]

    # Penghapusan Stopword
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if not word in stop_words]

    # # Stemming
    # stemmer = PorterStemmer()
    # tokens = [stemmer.stem(word) for word in tokens]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)

# apply clean text
def cleaner(data):
    data['text_preprocessed'] = data['description'].apply(clean_text)
    return data

# Recomendation 1
def recommend_restaurants(data, query, top_n=5):

    data = cleaner(data)

    # Preprocess the query
    query_cleaned = clean_text(query)

    # TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['text_preprocessed'])

    # Transform the query to TF-IDF
    query_tfidf = tfidf_vectorizer.transform([query_cleaned])

    # Compute cosine similarity
    cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

    # Get top N recommendations
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]

    # Create a list to put top restaurants
    recommend_restaurant = [data.iloc[idx]['name'] for idx in top_indices]

    # Creating the new DataFrame with filter
    dat_for_filter = data[data['name'].isin(recommend_restaurant)]

    return dat_for_filter

# Filter-------------------

# Recomendation filtering
def recSystem_Filter(data, query, df_filter, top_n=3):

    data = cleaner(data)

    # Preprocess the query
    query_cleaned = clean_text(query)

    # TF-IDF Vectorization
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['text_preprocessed'])

    # Transform the query to TF-IDF
    query_tfidf = tfidf_vectorizer.transform([query_cleaned])

    # Compute cosine similarity
    cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

    # Get top N recommendations
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]

    # Create a list to put top restaurants
    recommend_restaurant = []

    # Find the top similar restaurants
    for idx in top_indices:
        recommend_restaurant.append(data.iloc[idx]['name'])

    # Creating the new DataFrame with filter
    dat_for_filter = df_filter[df_filter['name'].isin(recommend_restaurant)]

    return dat_for_filter


