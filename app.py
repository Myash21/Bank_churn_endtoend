import pickle
import numpy as np
import streamlit as st

# Load the model
classmodel = pickle.load(open('bank_churn.pkl', 'rb'))

# Function to predict churn
def predict_churn(data):
    input_data = np.array(list(data.values())).reshape(1, -1)
    output = classmodel.predict(input_data)[0]
    prediction_text = "Bank churn likely" if output == 1 else "Bank churn unlikely"
    return prediction_text

def main():
    st.title('Bank Churn Prediction')
    st.write('Enter the following details to predict whether a customer is likely to churn or not.')

    # Custom CSS styles
    st.markdown(
        """
        <style>
        .stTextInput>div>div>div>input {
            border-radius: 10px;
            border: 2px solid #007bff;
            padding: 10px;
            margin-bottom: 15px;
        }
        .stRadio>div>div>label>div>div {
            margin-right: 15px;
        }
        .stButton>button {
            border-radius: 10px;
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .prediction {
            text-align: center;
            font-size: 20px;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    credit_score = st.text_input("Credit Score")
    age = st.text_input("Age")
    tenure = st.text_input("Tenure")
    balance = st.text_input("Balance")
    num_of_products = st.text_input("NumOfProducts")
    has_cr_card = st.radio("HasCrCard", ("Yes", "No"))
    is_active_member = st.radio("IsActiveMember", ("Yes", "No"))
    estimated_salary = st.text_input("EstimatedSalary")
    france = st.radio("France", ("Yes", "No"))
    germany = st.radio("Germany", ("Yes", "No"))
    spain = st.radio("Spain", ("Yes", "No"))
    female = st.radio("Female", ("Yes", "No"))

    if st.button("Predict"):
        if '' in [credit_score, age, tenure, balance, num_of_products, estimated_salary]:
            st.error("Please fill in all the required fields.")
        else:
            data = {
                'CreditScore': float(credit_score),
                'Age': float(age),
                'Tenure': float(tenure),
                'Balance': float(balance),
                'NumOfProducts': float(num_of_products),
                'HasCrCard': 1 if has_cr_card == "Yes" else 0,
                'IsActiveMember': 1 if is_active_member == "Yes" else 0,
                'EstimatedSalary': float(estimated_salary),
                'France': 1 if france == "Yes" else 0,
                'Germany': 1 if germany == "Yes" else 0,
                'Spain': 1 if spain == "Yes" else 0,
                'Female': 1 if female == "Yes" else 0
            }
            prediction = predict_churn(data)
            st.write("Prediction:", prediction)

if __name__ == "__main__":
    main()
