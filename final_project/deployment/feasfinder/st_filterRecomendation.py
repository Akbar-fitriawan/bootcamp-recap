import streamlit as st
import pandas as pd
from recomendation import recSystem_Filter

# Load Data 
df = pd.read_csv('trip_clean.csv')

# Filter DataFrame
def filter_dataframe(df, types, price_ranges, cities):
    if types:
        df = df[df[['type1', 'type2', 'type3']].apply(lambda row: any(t in types for t in row if t), axis=1)]
    if price_ranges:
        df = df[df['price_range'].isin(price_ranges)]
    if cities:
        df = df[df['city'].isin(cities)]
    return df

def beta():
    # Streamlit App
    st.title('Restaurant Data Filtering 🍽️✨')

    # Initialize session state for selected types
    if 'selected_types' not in st.session_state:
        st.session_state.selected_types = []

    # Callback function to update selected types
    def update_selected_types():
        if len(st.session_state.selected_types) > 3:
            st.warning('You can select up to 3 types only.')
            st.session_state.selected_types = st.session_state.selected_types[:3]

    # Multiselect for filtering food types
    selected_types = st.multiselect(
        'Select types (max 3)',
        options=pd.unique(df[['type1', 'type2', 'type3']].values.ravel('K')),
        default=st.session_state.selected_types,
        on_change=update_selected_types,
        key='selected_types'
    )

    # Selectbox for filtering price range
    selected_price_ranges = st.selectbox('Select price range', options=[''] + list(df['price_range'].unique()), index=0)

    # Selectbox for filtering city
    selected_cities = st.selectbox('Select city', options=[''] + list(df['city'].unique()), index=0)

    # Filter DataFrame based on user selection
    filtered_df = filter_dataframe(df, selected_types, [selected_price_ranges] if selected_price_ranges else [], [selected_cities] if selected_cities else [])

    data_filter = filtered_df.copy()

    if data_filter.empty:
        st.warning('Data is not available in the dataset.')
    else:
        st.write(data_filter)

    st.divider()

    # Input from user
    query = st.text_input('Enter a restaurant name or description')

    if st.button('Get Recommendations'):
        if query.strip() == "":
            st.warning("Please enter a keyword or description to get recommendations based on similarity.")
        else:
            recommendations = recSystem_Filter(df, query, data_filter)
            if not recommendations.empty:
                st.write('### **Results Top restaurant recommendations**🤩')
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
    beta()
