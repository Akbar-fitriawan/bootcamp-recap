import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recommendations(restaurant_type=None, comments=None, city=None, state=None, price=None, num_recommendations=5):
    # Filter restaurants based on multiple inputs
    filtered_restaurants = pd.read_csv('trip_clean.csv')
    if restaurant_type:
        filtered_restaurants = filtered_restaurants[filtered_restaurants['type1'] == restaurant_type]
    if comments:
        filtered_restaurants = filtered_restaurants[filtered_restaurants['comments'].str.contains(comments)]
    if city:
        filtered_restaurants = filtered_restaurants[filtered_restaurants['city'] == city]
    if state:
        filtered_restaurants = filtered_restaurants[filtered_restaurants['state'] == state]
    if price:
        filtered_restaurants = filtered_restaurants[filtered_restaurants['price_range'].isin(price)]

    # Create a new TfidfVectorizer instance
    tfidf_filtered = TfidfVectorizer()
    
    # Fit and transform the filtered data
    tfidf_matrix_filtered = tfidf_filtered.fit_transform(filtered_restaurants['text_preprocessed'])
    
    # Calculate cosine similarity between the filtered restaurants
    cosine_sim_filtered = cosine_similarity(tfidf_matrix_filtered)
    
    # Get the average similarity score for each restaurant
    avg_sim_scores = cosine_sim_filtered.mean(axis=0)
    
    # Get the top N most similar restaurants
    top_recommendations = avg_sim_scores.argsort()[:-num_recommendations-1:-1]
    
    # List of output column to display
    output_col = ['name','street_address','city','state']

    # Update output column into the dataset
    filtered_restaurants = filtered_restaurants[output_col]

    # Create output of the recommended restaurant information
    output = filtered_restaurants.iloc[top_recommendations]

    # Reset the index and drop the old index
    output = output.reset_index(drop=True)

    # Set the index to a new range starting from 1
    output.index = range(1, len(output)+1)

    # Return output
    return output
