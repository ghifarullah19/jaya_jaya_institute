import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from predictions import predictions

st.title('Student Dropout Prediction')

st.write('This is a simple web app to predict student dropout based on the student data provided.')

st.write('Please provide the student data in the form below:')

data = pd.DataFrame()

Admission_grade = st.number_input('Admission Grade', min_value=0, max_value=200)
data['Admission_grade'] = [Admission_grade]
Age_at_enrollment = st.number_input('Age at Enrollment', min_value=16, max_value=70)
data['Age_at_enrollment'] = [Age_at_enrollment]
Application_mode = st.selectbox('Application Mode', [1, 2, 5, 7, 10, 16, 17, 18, 26, 27, 39, 43, 44, 51, 53, 57])
data['Application_mode'] = [Application_mode]
Application_order = st.selectbox('Application Order', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
data['Application_order'] = [Application_order]

Curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Semester Approved', min_value=0, max_value=100)
data['Curricular_units_1st_sem_approved'] = [Curricular_units_1st_sem_approved]
Curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Semester Enrolled', min_value=0, max_value=100)
data['Curricular_units_1st_sem_enrolled'] = [Curricular_units_1st_sem_enrolled]
Curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Semester Evaluations', min_value=0, max_value=100)
data['Curricular_units_1st_sem_evaluations'] = [Curricular_units_1st_sem_evaluations]
Curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Semester Grade', min_value=0, max_value=20)
data['Curricular_units_1st_sem_grade'] = [Curricular_units_1st_sem_grade]
Curricular_units_1st_sem_without_evaluations = st.number_input('Curricular Units 1st Semester Without Evaluations', min_value=0, max_value=100)
data['Curricular_units_1st_sem_without_evaluations'] = [Curricular_units_1st_sem_without_evaluations]

Curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Semester Approved', min_value=0, max_value=100)
data['Curricular_units_2nd_sem_approved'] = [Curricular_units_2nd_sem_approved]
Curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Semester Enrolled', min_value=0, max_value=100)
data['Curricular_units_2nd_sem_enrolled'] = [Curricular_units_2nd_sem_enrolled]
Curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Semester Evaluations', min_value=0, max_value=100)
data['Curricular_units_2nd_sem_evaluations'] = [Curricular_units_2nd_sem_evaluations]
Curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Semester Grade', min_value=0, max_value=20)
data['Curricular_units_2nd_sem_grade'] = [Curricular_units_2nd_sem_grade]
Curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular Units 2nd Semester Without Evaluations', min_value=0, max_value=100)
data['Curricular_units_2nd_sem_without_evaluations'] = [Curricular_units_2nd_sem_without_evaluations]

Daytime_evening_attendance = st.selectbox('Daytime/Evening Attendance', [0, 1])
data['Daytime_evening_attendance'] = [Daytime_evening_attendance]
Debtor = st.selectbox('Debtor', [0, 1])
data['Debtor'] = [Debtor]
Displaced = st.selectbox('Displaced', [0, 1])
data['Displaced'] = [Displaced]

Gender = st.selectbox('Gender', [0, 1])
data['Gender'] = [Gender]
Marital_status = st.selectbox('Marital Status', [1, 2, 3, 4, 5, 6])
data['Marital_status'] = [Marital_status]
Mothers_qualification = st.selectbox("Mother's Qualification", [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
data['Mothers_qualification'] = [Mothers_qualification]

Previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0, max_value=200)
data['Previous_qualification_grade'] = [Previous_qualification_grade]
Scholarship_holder = st.selectbox('Scholarship Holder', [0, 1])
data['Scholarship_holder'] = [Scholarship_holder]
Tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date', [0, 1])
data['Tuition_fees_up_to_date'] = [Tuition_fees_up_to_date]

with st.expander('View the Raw Data'):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    data = data_preprocessing(data)
    with st.expander('View the Preprocessed Data'):
        st.dataframe(data=data, width=800, height=10)
    result = predictions(data)
    st.write(f'The student is predicted to: {result}')