import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import pickle
import json




def run():
    # load data
    df = pd.read_csv(r'employee-attrition.csv')

    st.title('Welcome to Exploratory Data Analysis :chart_with_upwards_trend:')
    
    st.subheader('Looking Dataframe')
    st.table(df.head(5))

    st.subheader("Summary Statistic")
    st.write("Summary Data")
    st.write(df.describe())
    st.write("Summary Top Frequency")
    st.write(df.describe(include=['object']))

    # Visualisasi by attrition
    st.subheader('History Attrition Employee')
    pie_data = df.Attrition.value_counts()
    fig = px.pie(names=pie_data.index, values=pie_data.values, title='Attriton Employee', labels=['No',"Yes"])
    st.plotly_chart(fig)

    # menampilkan penjelasan 
    with st.expander('Explanation'):
        employee_out = pie_data['Yes'] / sum(pie_data) * 100
        employee_stay = pie_data['No'] / sum(pie_data) * 100
        st.caption(f'Dari plot di atas {employee_out:.1f}% karyawan keluar dan {employee_stay:.1f}% yang tetap tinggal, target prediksi imbalnced atau tidak seimbang sehingga harus penyasuaian parameter atau metode lain untuk mengatasinya.')


    # Visualisasi by Job Satisfaction
    st.subheader("Looking Job Satisfaction")
    jobSatisfaction = df['JobSatisfaction'].value_counts()
    fig = px.pie(names=jobSatisfaction.index, values=jobSatisfaction.values, title="Employee Job Satisfaction", hole=0.65)
    st.plotly_chart(fig)
    # menampilkan penjelasan 
    with st.expander('Explanation'):
        low = jobSatisfaction['Low'] / sum(jobSatisfaction) * 100
        medium = jobSatisfaction['Medium'] / sum(jobSatisfaction) * 100
        high = jobSatisfaction['High'] / sum(jobSatisfaction) * 100
        veryHigh = jobSatisfaction['Very High'] / sum(jobSatisfaction) * 100
        st.caption(f'Job satisfaction menunjukkan karyawan tidak puas adalah {low:.1f}%, netral {medium:.1f}%, cukup puas {high:.1f}%, dan sangat puas {veryHigh:.1f}%')
    
    # Visualisasi mean by job role
    st.subheader("So, looking job role by income")
    mean_monthlyIncome = df.groupby(by='JobRole')['MonthlyIncome'].mean().reset_index()
    fig = px.bar(mean_monthlyIncome, x='JobRole', y='MonthlyIncome',title="Mean Income by Job Role")
    st.plotly_chart(fig)

    with st.expander("Explanation"):
        st.caption("Lorem ipsum")
    
    # Visualisasi by monthly Income
    st.subheader("Looking Distribution Monthly Income")

    # visualisasi total income depertment
    total_incomeByDepartment = df.groupby(by='Department')['MonthlyIncome'].sum().reset_index()
    fig = px.bar(total_incomeByDepartment, x='Department', y='MonthlyIncome', title="Total Income by Department")
    st.plotly_chart(fig)

    # visualisasi count employee by department
    count_incomeByDepartment = df['Department'].value_counts().reset_index()
    count_incomeByDepartment.columns = ['Department','Employee Count']
    fig = px.bar(count_incomeByDepartment,  x='Department', y='Employee Count', title="Employee Count by Department")
    st.plotly_chart(fig)


if __name__ == "__main__":
    run()