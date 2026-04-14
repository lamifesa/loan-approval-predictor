# Import libraries
import streamlit as st
import pandas as pd
import sklearn
import joblib

# loading saved model
@st.cache_resource
def load_model():
    return joblib.load('randomforestclassifier.pkl')

model = load_model()
# Add this right after model = load_model()
# List of features in order
# st.write(model.feature_names_in_.tolist())

# print(model)

# Create dictonary of features
feature_dict = dict()

# Encoding maps
gender_map = {"Female": 0, "Male": 1, "Other": 2}
marital_map = {"Divorced": 0, "Married": 1, "Single": 2, "Widowed": 3}
education_map = {"Bachelor's": 0, "High School": 1, "Master's": 2, "Other": 3, "PhD": 4}
employment_map = {"Employed": 0, "Retired": 1, "Self-employed": 2, "Student": 3, "Unemployed": 4}
loan_purpose_map = {"Business": 0, "Car": 1, "Debt consolidation": 2, "Education": 3,
                    "Home": 4, "Medical": 5, "Other": 6, "Vacation": 7}

subgrade_list = sorted([i + str(j) for i in ['A','B','C','D','E','F'] for j in range(1,6)])
grade_subgrade_map = {v: i for i, v in enumerate(subgrade_list)}

# starting form
st.header("Loan Eligibility Predictor")
with st.form("loan_form"):
    
    st.write("Are you eligible for a loan? Find out below.")

    name = st.text_input("Name:",)
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender:", list(gender_map.keys()))
        age = st.slider("Age:", min_value=18, max_value=100, value=30)
        marital_status = st.selectbox("Marital Status:", list(marital_map.keys()))
        education_level = st.selectbox("Education Level:", list(education_map.keys()))
        employment_status = st.selectbox("Employment Status:", list(employment_map.keys()))
        annual_income = st.number_input("Annual Income (€):", min_value=0.0)
        debt_to_income_ratio = st.number_input("Debt-to-Income Ratio:", min_value=0.0, max_value=1.0, step=0.001, format="%.3f")
        credit_score = st.number_input("Credit Score:", min_value=300, max_value=850, value=650)
        loan_amount = st.number_input("Loan Amount (€):", min_value=0.0)
        loan_purpose = st.selectbox("Loan Purpose:", list(loan_purpose_map.keys()))

    with col2:
        interest_rate = st.number_input("Interest Rate (%):", min_value=0.0)
        loan_term = st.radio("Loan Term (months):", [36, 60])
        installment = st.number_input("Monthly Installment (€):", min_value=0.0)
        grade_subgrade = st.selectbox("Grade-Subgrade:", subgrade_list)
        num_of_open_accounts = st.slider("Number of Open Accounts:", 0, 15)
        total_credit_limit = st.number_input("Total Credit Limit (€):", min_value=0.0)
        current_balance = st.number_input("Current Balance (€):", min_value=0.0)
        delinquency_history = st.slider("Delinquency History:", 0, 11)
        public_records = st.slider("Public Records:", 0, 2)
        num_of_delinquencies = st.slider("Number of Delinquencies:", 0, 11)

    # Submit button
    submit_button = st.form_submit_button("Check Eligibility")

    
    
    if submit_button:
        monthly_income = annual_income / 12

        # Creating dataframe for the model
        input_data = pd.DataFrame([{
            'age': age,
            'gender': gender_map[gender],
            'marital_status': marital_map[marital_status],
            'education_level': education_map[education_level],
            'annual_income': annual_income,
            'monthly_income': monthly_income,
            'employment_status': employment_map[employment_status],
            'debt_to_income_ratio': debt_to_income_ratio,
            'credit_score': credit_score,
            'loan_amount': loan_amount,
            'loan_purpose': loan_purpose_map[loan_purpose],
            'interest_rate': interest_rate,
            'loan_term': loan_term,
            'installment': installment,
            'grade_subgrade': grade_subgrade_map[grade_subgrade],
            'num_of_open_accounts': num_of_open_accounts,
            'total_credit_limit': total_credit_limit,
            'current_balance': current_balance,
            'delinquency_history': delinquency_history,
            'public_records': public_records,
            'num_of_delinquencies': num_of_delinquencies,
        }])
        
        prediction = model.predict(input_data)[0]
        display_name = name.title() if name else "You"

        st.divider()
        if prediction == 1:
            st.success(f"{display_name}, you are **likely eligible** for this loan")
        else:
            st.error(f"{display_name}, you are **unlikely to be eligible** for this loan")
