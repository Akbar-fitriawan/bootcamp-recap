import streamlit as st
import numpy as np
import pandas as pd
import pickle





def generate_dummy_data(num_rows):
    data = {
        'limit_balance': np.random.randint(5000, 100000, num_rows),
        'sex': np.random.choice([1, 2], num_rows),
        'education_level': np.random.choice([1, 2, 3 ,4], num_rows),
        'marital_status': np.random.choice([1,2,3,0], num_rows),
        'age': np.random.randint(18, 70, num_rows),
        'pay_0': np.random.randint(-2, 8, num_rows),
        'pay_2': np.random.randint(-2, 8, num_rows),
        'pay_3': np.random.randint(-2, 8, num_rows),
        'pay_4': np.random.randint(-2, 8, num_rows),
        'pay_5': np.random.randint(-2, 8, num_rows),
        'pay_6': np.random.randint(-2, 8, num_rows),
        'bill_amt_1': np.random.randint(0, 100000, num_rows),
        'bill_amt_2': np.random.randint(0, 100000, num_rows),
        'bill_amt_3': np.random.randint(0, 100000, num_rows),
        'bill_amt_4': np.random.randint(0, 100000, num_rows),
        'bill_amt_5': np.random.randint(0, 100000, num_rows),
        'bill_amt_6': np.random.randint(0, 100000, num_rows),
        'pay_amt_1': np.random.randint(0, 30000, num_rows),
        'pay_amt_2': np.random.randint(0, 30000, num_rows),
        'pay_amt_3': np.random.randint(0, 30000, num_rows),
        'pay_amt_4': np.random.randint(0, 30000, num_rows),
        'pay_amt_5': np.random.randint(0, 30000, num_rows),
        'pay_amt_6': np.random.randint(0, 30000, num_rows),
        'default_payment_next_month': np.random.choice([0, 1], num_rows)
    }
    return pd.DataFrame(data)

def run():
    st.title("Predict Default Payment Next Month")

    # Load the model and preprocessing objects
    with open('knn_randomcv.pkl', 'rb') as file:
        knn_randomcv = pickle.load(file)

    with open('scaler.pkl', 'rb') as file2:
        scaler = pickle.load(file2)
    
    with open('list_cat_cols.pkl', 'rb') as file3:
        list_cat_cols = pickle.load(file3)

    with open('list_num_cols.pkl', 'rb') as file4:
        list_num_cols = pickle.load(file4)
    
    num_rows = st.slider("Select number of dummy data rows to generate", min_value=1, max_value=20, value=10)

    if st.button("Generate"):
        dummy_data = generate_dummy_data(num_rows)

        # Preprocess the generated dummy data
        dummy_data_num = dummy_data[list_num_cols]  
        dummy_data_cat = dummy_data[list_cat_cols]

        dummy_data_num_scaled = scaler.transform(dummy_data_num,dummy_data_cat)

        dummy_data_final = np.concatenate([dummy_data_num_scaled, dummy_data_cat], axis=1)

        # Make predictions
        predictions = knn_randomcv.predict(dummy_data_final)
        dummy_data['predicted_default'] = predictions

        st.write(dummy_data)

if __name__ == '__main__':
    run()
