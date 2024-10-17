import streamlit as st
import pandas as pd
import pickle
import joblib

# Load the trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


def main():
    st.title("Employee Attrition Prediction")


    st.markdown('## 📝 Input Data')
    with st.form('my_form'):

        age = st.slider("Age", 18, 59)
        business_travel = st.selectbox("Business Travel", ['Travel_Rarely', 'Non-Travel', 'Travel_Frequently'])
        department = st.selectbox("Department", ['Research & Development', 'Sales', 'Human Resources'])
        distance_from_home = st.slider("Distance From Home", 2, 29)
        education = st.slider("Education", 1, 5)
        education_field = st.selectbox("Education Field", ['Marketing', 'Technical Degree', 'Life Sciences', 'Medical', 'Human Resources', 'Other'])
        gender = st.radio("Gender", ['Female', 'Male'])
        job_role = st.selectbox("Job Role", ['Sales Executive', 'Manufacturing Director', 'Healthcare Representative', 'Research Scientist', 'Laboratory Technician', 'Human Resources', 'Sales Representative', 'Research Director', 'Manager'])
        job_satisfaction = st.selectbox("Job Satisfaction", ['Low', 'Medium', 'High', 'Very High'])
        marital_status = st.selectbox("Marital Status", ['Divorced', 'Married', 'Single'])
        monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=200000)
        num_companies_worked = st.slider("Number of Companies Worked", 1, 10)
        percent_salary_hike = st.slider("Percent Salary Hike", 10, 25)
        performance_rating = st.slider("Performance Rating", 3, 4)
        total_working_years = st.slider("Total Working Years", 1, 35)
        work_life_balance = st.selectbox("Work Life Balance", ['Better', 'Bad', 'Good', 'Best'])
        years_at_company = st.slider("Years At Company", 1, 35)
        years_in_current_role = st.slider("Years In Current Role", 1, 17)
        years_since_last_promotion = st.slider("Years Since Last Promotion", 1, 15)
        years_with_current_manager = st.slider("Years With Current Manager", 1, 17)

        submitted = st.form_submit_button('Let\'s 🔍 Check ')

    input_data = pd.DataFrame({
        'Age':[age],
        'BusinessTravel':[business_travel],
        'Department':[department],
        'DistanceFormHome':[distance_from_home],
        'Education':[education],
        'EducationField':[education_field],
        'Gender':[gender],
        'JobRole':[job_role],
        'JobSatisfaction':[job_satisfaction],
        'MaritalStatus':[marital_status],
        'MonthlyIncome':[monthly_income],
        'NumCompaniesWorked':[num_companies_worked],
        'PercentSalaryHike':[percent_salary_hike],
        'PerformanceRating':[performance_rating],
        'TotalWorkingYears':[total_working_years],
        'YearsAtCompany':[years_at_company],
        'YearsInCurrentRole':[years_in_current_role],
        'YearsSinceLastPromotion':[years_since_last_promotion],
        'YearsWithCurrentManager':[years_with_current_manager]
    })

    st.markdown('Syntetic Dataframe')
    st.dataframe(input_data)


    st.markdown('Prediction')
    if submitted:
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            st.write('🟢 Employee is not likely to leave')
        else:
            st.write('🔴 Employee is likely to leave')

if __name__ == "__main__":
    main()
