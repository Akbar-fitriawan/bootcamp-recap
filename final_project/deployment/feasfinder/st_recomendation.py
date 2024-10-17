import streamlit as st
import pandas as pd
from recomendation import recommend_restaurants

# Load Data
data = pd.read_csv('trip_clean.csv')

def alpha():
    # Streamlit UI
    st.title('Restaurant Recommendation System 🍽️✨')

    # Input from user
    query = st.text_input('Enter a restaurant name or description')

    if st.button('Get Recommendations'):
        recommendations = recommend_restaurants(data, query, top_n=5)
        if not recommendations.empty:
            st.write('### **Results Top 5 restaurant recommendations**🤩')
            st.divider()

            for _, row in recommendations.iterrows():
                st.write(f'### {row["name"]}')
                st.write(f'Reviews: {row["reviews"]}/5')
                st.write(f'Price Range: {row["price_range"]}')
                st.write(f'Address: {row["street_address"]}, {row["city"]}, {row["state"]}')
                st.write('\n')
                st.divider()
    
        else:
            st.write('No recommendations found.')

if __name__ == "__main__":
    alpha()
