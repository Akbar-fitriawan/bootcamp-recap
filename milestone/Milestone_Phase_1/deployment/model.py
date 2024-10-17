import streamlit as st
import numpy as np
import pandas as pd
import pickle


# Load the trained model
with open("ranfo_pipe.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def run():

    # Streamlit UI
    st.title("Insurance Claims over Cars")

    # Introduction
    st.subheader("📊 Prediction Insurance Claim or NO ")

    st.markdown('## 📝 Input Data')
    with st.form('my_form'):

        # Age
        age_choice = st.selectbox("Age", ['Young', 'Middle Age', 'Old', 'Very Old'])
        # Gender
        gender_choice = st.selectbox("Gender", ['male', 'female'])
        # Race
        race_choice = st.selectbox("Race", ['Majority', 'Minority'])
        # Driving Experience
        driving_experience_choice = st.selectbox("Driving Experience", ['Newbie', 'Amateur', 'Advanced', 'Expert'])
        # Education
        education_choice = st.selectbox("Education", ['high school', 'none', 'university'])
        # Income
        income_choice = st.selectbox("Income", ['upper class', 'poverty', 'working class', 'middle class'])
        # Credit Score Range
        credit_score_range = st.number_input("Credit Score Range", min_value=0.0, max_value=999999.0)
        # Vehicle Ownership
        vehicle_ownership_choice = st.selectbox("Vehicle Ownership (True/False)", [0.0, 1.0])
        # Vehicle Year
        vehicle_year_choice = st.selectbox("Vehicle Year", ['before 2015', 'after 2015'])
        # Married
        married_choice = st.selectbox("Married (True/False)", [0.0, 1.0])
        # Children
        children_choice = st.selectbox("Children (True/False)", [0.0, 1.0])
        # Postal Code
        postal_code_choice = st.selectbox("Postal Code", [10238, 32765, 92101, 21217])
        # Annual Mileage Range
        annual_mileage_range = st.number_input("Annual Mileage Range", min_value=0, max_value=999999)
        # Vehicle Type
        vehicle_type_choice = st.selectbox("Vehicle Type", ['sedan', 'sport car'])
        # Speeding Violations Range
        speeding_violations_range = st.number_input("Speeding Violations Range", min_value=0, max_value=50)
        # DUIs Range
        duis_range = st.number_input("DUIs Range", min_value=0, max_value=50)
        # Past Accidents Range
        past_accidents_range = st.number_input("Past Accidents Range", min_value=0, max_value=50)

        submitted = st.form_submit_button('🔍 Let\'s Check!')

    # Create DataFrame from user input
    data = {
            "AGE":age_choice,
            "GENDER":gender_choice,
            "RACE":race_choice,
            "DRIVING_EXPERIENCE":driving_experience_choice,
            "EDUCATION":education_choice,
            "INCOME":income_choice,
            "CREDIT_SCORE":credit_score_range,
            "VEHICLE_OWNERSHIP":vehicle_ownership_choice,
            "VEHICLE_YEAR":vehicle_year_choice,
            "MARRIED":married_choice,
            "CHILDREN":children_choice,
            "POSTAL_CODE":postal_code_choice,
            "ANNUAL_MILEAGE":annual_mileage_range,
            "VEHICLE":vehicle_type_choice,
            "SPEEDING_VIOLATIONS":speeding_violations_range,
            "DUIS":duis_range,
            "PAST_ACCIDENTS":past_accidents_range,
            }

    df = pd.DataFrame([data])
    st.dataframe(df)

    # Make prediction
    if submitted:
        prediction = model.predict(df)
        # Display prediction result
        if prediction[0] == 0:
            st.write('🟢 Claims loan')
        else:
            st.write('🔴 No Loan')

if __name__=='__main__':
    run()
