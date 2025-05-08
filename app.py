import streamlit as st
import pandas as pd
import joblib


model = joblib.load('student_predict.pkl')


st.set_page_config(page_title="Student Dropout Predictor", layout="wide")
st.title("🎓 Student Dropout Prediction System")
st.markdown("""
This tool predicts whether a student status is dropping out or not based on academic and personal characteristics.
All fields marked with * are required.
""")

# ===== FORM =====
with st.form("student_form"):
    cols = st.columns(4)
    
    
    with cols[0]:
        st.subheader("Personal Information")
        age = st.number_input("Age at Enrollment*", min_value=17, max_value=70, value=20)
        gender = st.radio("Gender*", options=[("Male", 1), ("Female", 0)], format_func=lambda x: x[0])
        marital_status = st.selectbox("Marital Status*", options=[
            (1, "Single"), (2, "Married"), (3, "Widower"), 
            (4, "Divorced"), (5, "Facto Union"), (6, "Legally Separated")
        ], format_func=lambda x: x[1])
        international = st.radio("International Student*", options=[("No", 0), ("Yes", 1)], format_func=lambda x: x[0])
        displaced = st.radio("Displaced*", options=[("No", 0), ("Yes", 1)], format_func=lambda x: x[0])
        special_needs = st.radio("Educational Special Needs*", options=[("No", 0), ("Yes", 1)], format_func=lambda x: x[0])
    
    
    with cols[1]:
        st.subheader("Academic Background")
        application_mode = st.selectbox("Application Mode*", options=[
            (1, "1st phase - general contingent"), 
            (2, "Ordinance No. 612/93"),
            (5, "1st phase - special contingent (Azores Island)"),
            (7, "Holders of other higher courses"),
            (10, "Ordinance No. 854-B/99"),
            (15, "International student (bachelor)"),
            (16, "1st phase - special contingent (Madeira Island)"),
            (17, "2nd phase - general contingent"),
            (18, "3rd phase - general contingent"),
            (26, "Ordinance No. 533-A/99, item b2) (Different Plan)"),
            (27, "Ordinance No. 533-A/99, item b3 (Other Institution)"),
            (39, "Over 23 years old"),
            (42, "Transfer"),
            (43, "Change of course"),
            (44, "Technological specialization diploma holders"),
            (51, "Change of institution/course"),
            (53, "Short cycle diploma holders"),
            (57, "Change of institution/course (International)")
        ], format_func=lambda x: x[1])
        
        application_order = st.number_input("Application Order*", min_value=0, max_value=9, value=0,
                                         help="0 = first choice, 9 = last choice")
        
        prev_qualification = st.selectbox("Previous Qualification*", options=[
            (1, "Secondary education"), 
            (2, "Higher education - bachelor's degree"),
            (3, "Higher education - degree"),
            (4, "Higher education - master's"),
            (5, "Higher education - doctorate"),
            (6, "Frequency of higher education"),
            (9, "12th year of schooling - not completed"),
            (10, "11th year of schooling - not completed"),
            (12, "Other - 11th year of schooling"),
            (14, "10th year of schooling"),
            (15, "10th year of schooling - not completed"),
            (19, "Basic education 3rd cycle"),
            (38, "Basic education 2nd cycle"),
            (39, "Technological specialization course"),
            (40, "Higher education - degree (1st cycle)"),
            (42, "Professional higher technical course"),
            (43, "Higher education - master (2nd cycle)")
        ], format_func=lambda x: x[1])
        
        prev_grade = st.number_input("Previous Qualification Grade*", min_value=0, max_value=200, value=0)
        admission_grade = st.number_input("Admission Grade*", min_value=0, max_value=200, value=0)
    
    
    with cols[2]:
        st.subheader("Family Background")
        nationality = st.selectbox("Nationality*", options=[
            (1, "Portuguese"), (2, "German"), (6, "Spanish"), 
            (11, "Italian"), (13, "Dutch"), (14, "English"),
            (17, "Lithuanian"), (21, "Angolan"), (22, "Cape Verdean"),
            (24, "Guinean"), (25, "Mozambican"), (26, "Santomean"),
            (32, "Turkish"), (41, "Brazilian"), (62, "Romanian"),
            (100, "Moldova (Republic of)"), (101, "Mexican"), 
            (103, "Ukrainian"), (105, "Russian"), (108, "Cuban"),
            (109, "Colombian")
        ], format_func=lambda x: x[1])
        
        mothers_qual = st.selectbox("Mother's Qualification", options=[
            (1, "Secondary Education - 12th Year"),
            (2, "Higher Education - Bachelor's"),
            (3, "Higher Education - Degree"),
            (4, "Higher Education - Master's"),
            (5, "Higher Education - Doctorate"),
            (6, "Frequency of Higher Education"),
            (9, "12th Year - Not Completed"),
            (10, "11th Year - Not Completed"),
            (11, "7th Year (Old)"),
            (12, "Other - 11th Year"),
            (14, "10th Year"),
            (18, "General commerce course"),
            (19, "Basic Education 3rd Cycle"),
            (22, "Technical-professional course"),
            (26, "7th year of schooling"),
            (27, "2nd cycle general high school"),
            (29, "9th Year - Not Completed"),
            (30, "8th year of schooling"),
            (34, "Unknown"),
            (35, "Can't read or write"),
            (36, "Can read without 4th year"),
            (37, "Basic education 1st cycle"),
            (38, "Basic Education 2nd Cycle"),
            (39, "Technological specialization"),
            (40, "Higher education - degree"),
            (41, "Specialized higher studies"),
            (42, "Professional higher technical"),
            (43, "Higher Education - Master"),
            (44, "Higher Education - Doctorate")
        ], format_func=lambda x: x[1], index=0)
        
        fathers_qual = st.selectbox("Father's Qualification", options=[
            (1, "Secondary Education - 12th Year"),
            (2, "Higher Education - Bachelor's"),
            (3, "Higher Education - Degree"),
            (4, "Higher Education - Master's"),
            (5, "Higher Education - Doctorate"),
            (6, "Frequency of Higher Education"),
            (9, "12th Year - Not Completed"),
            (10, "11th Year - Not Completed"),
            (11, "7th Year (Old)"),
            (12, "Other - 11th Year"),
            (13, "2nd year complementary HS"),
            (14, "10th Year"),
            (18, "General commerce course"),
            (19, "Basic Education 3rd Cycle"),
            (20, "Complementary HS Course"),
            (22, "Technical-professional course"),
            (25, "Complementary HS - not concluded"),
            (26, "7th year of schooling"),
            (27, "2nd cycle general high school"),
            (29, "9th Year - Not Completed"),
            (30, "8th year of schooling"),
            (31, "General Admin/Commerce"),
            (33, "Supplementary Accounting"),
            (34, "Unknown"),
            (35, "Can't read or write"),
            (36, "Can read without 4th year"),
            (37, "Basic education 1st cycle"),
            (38, "Basic Education 2nd Cycle"),
            (39, "Technological specialization"),
            (40, "Higher education - degree"),
            (41, "Specialized higher studies"),
            (42, "Professional higher technical"),
            (43, "Higher Education - Master"),
            (44, "Higher Education - Doctorate")
        ], format_func=lambda x: x[1], index=0)
        
        mothers_occ = st.selectbox("Mother's Occupation", options=[
            (0, "Student"), 
            (1, "Legislative/Executive Managers"),
            (2, "Intellectual/Scientific Specialists"),
            (3, "Intermediate Technicians"),
            (4, "Administrative staff"),
            (5, "Personal Services/Security/Sellers"),
            (6, "Skilled Agriculture/Fishery"),
            (7, "Skilled Industry/Construction"),
            (8, "Machine Operators"),
            (9, "Unskilled Workers"),
            (10, "Armed Forces"),
            (90, "Other Situation"),
            (99, "(blank)"),
            (122, "Health professionals"),
            (123, "Teachers"),
            (125, "ICT specialists"),
            (131, "Science/Engineering technicians"),
            (132, "Health technicians"),
            (134, "Legal/Social/Cultural technicians"),
            (141, "Office workers"),
            (143, "Accounting/Financial operators"),
            (144, "Other admin support"),
            (151, "Personal service workers"),
            (152, "Sellers"),
            (153, "Personal care workers"),
            (171, "Skilled construction workers"),
            (173, "Skilled manufacturing workers"),
            (175, "Food/Clothing industry workers"),
            (191, "Cleaning workers"),
            (192, "Unskilled agriculture workers"),
            (193, "Unskilled industry workers"),
            (194, "Meal preparation assistants")
        ], format_func=lambda x: x[1], index=0)
        
        fathers_occ = st.selectbox("Father's Occupation", options=[
            (0, "Student"), 
            (1, "Legislative/Executive Managers"),
            (2, "Intellectual/Scientific Specialists"),
            (3, "Intermediate Technicians"),
            (4, "Administrative staff"),
            (5, "Personal Services/Security/Sellers"),
            (6, "Skilled Agriculture/Fishery"),
            (7, "Skilled Industry/Construction"),
            (8, "Machine Operators"),
            (9, "Unskilled Workers"),
            (10, "Armed Forces"),
            (90, "Other Situation"),
            (99, "(blank)"),
            (101, "Armed Forces Officers"),
            (102, "Armed Forces Sergeants"),
            (103, "Other Armed Forces"),
            (112, "Admin/Commercial directors"),
            (114, "Hotel/Trade services directors"),
            (121, "Science/Engineering specialists"),
            (122, "Health professionals"),
            (123, "Teachers"),
            (124, "Finance/Admin specialists"),
            (131, "Science/Engineering technicians"),
            (132, "Health technicians"),
            (134, "Legal/Social technicians"),
            (135, "ICT technicians"),
            (141, "Office workers"),
            (143, "Accounting/Financial operators"),
            (144, "Other admin support"),
            (151, "Personal service workers"),
            (152, "Sellers"),
            (153, "Personal care workers"),
            (154, "Protection services"),
            (161, "Skilled agriculture workers"),
            (163, "Subsistence farmers/fishermen"),
            (171, "Skilled construction workers"),
            (172, "Skilled metal workers"),
            (174, "Skilled electricians"),
            (175, "Food/Clothing industry workers"),
            (181, "Machine operators"),
            (182, "Assembly workers"),
            (183, "Vehicle drivers"),
            (192, "Unskilled agriculture workers"),
            (193, "Unskilled industry workers"),
            (194, "Meal preparation assistants")
        ], format_func=lambda x: x[1], index=0)
    
    
    with cols[3]:
        st.subheader("Academic Details")
        course = st.selectbox("Course*", options=[
            (33, "Biofuel Production Technologies"),
            (171, "Animation and Multimedia Design"),
            (8014, "Social Service (evening)"),
            (9003, "Agronomy"),
            (9070, "Communication Design"),
            (9085, "Veterinary Nursing"),
            (9119, "Informatics Engineering"),
            (9130, "Equinculture"),
            (9147, "Management"),
            (9238, "Social Service"),
            (9254, "Tourism"),
            (9500, "Nursing"),
            (9556, "Oral Hygiene"),
            (9670, "Advertising and Marketing"),
            (9773, "Journalism and Communication"),
            (9853, "Basic Education"),
            (9991, "Management (evening)")
        ], format_func=lambda x: x[1])
        
        attendance = st.radio("Daytime/Evening Attendance*", options=[("Daytime", 1), ("Evening", 0)], format_func=lambda x: x[0])
        
        st.markdown("**Financial Status**")
        debtor = st.checkbox("Debtor")
        tuition_fees = st.checkbox("Tuition Fees Up to Date")
        scholarship = st.checkbox("Scholarship Holder")
        
        st.markdown("**1st Semester Performance**")
        cu_1st_credited = st.number_input("Credited Units", min_value=0, value=0)
        cu_1st_enrolled = st.number_input("Enrolled Units", min_value=0, value=0)
        cu_1st_evaluations = st.number_input("Evaluated Units", min_value=0, value=0)
        cu_1st_wo_evaluations = st.number_input("Without Evaluated Units", min_value=0, value=0)
        cu_1st_approved = st.number_input("Approved Units", min_value=0, value=0)
        cu_1st_grade = st.number_input("Average Grade", min_value=0.0, max_value=20.0, value=10.0)
        
        st.markdown("**2nd Semester Performance**")
        cu_2nd_credited = st.number_input("Credited Units ", min_value=0, value=0)
        cu_2nd_enrolled = st.number_input("Enrolled Units ", min_value=0, value=0)
        cu_2nd_evaluations = st.number_input("Evaluated Units ", min_value=0, value=0)
        cu_2st_wo_evaluations = st.number_input("Without Evaluated Units",value=0)
        cu_2nd_approved = st.number_input("Approved Units ", min_value=0, value=0)
        cu_2nd_grade = st.number_input("Average Grade ", min_value=0.0, max_value=20.0, value=10.0)
    
    
    st.subheader("Economic Context")
    econ_cols = st.columns(3)
    with econ_cols[0]:
        unemployment = st.number_input("Unemployment Rate (%)", min_value=0.0, max_value=100.0, value=7.5)
    with econ_cols[1]:
        inflation = st.number_input("Inflation Rate (%)", min_value=-10.0, max_value=100.0, value=2.5)
    with econ_cols[2]:
        gdp = st.number_input("GDP Growth Rate (%)", min_value=-10.0, max_value=100.0, value=1.5)
    
    
    submitted = st.form_submit_button("Predict Dropout Risk")

# ===== PREDICTION =====
if submitted:
    
    input_data = {
        'Marital_status': marital_status[0],
        'Application_mode': application_mode[0],
        'Application_order': application_order,
        'Course': course[0],
        'Daytime_evening_attendance': attendance[1],
        'Previous_qualification': prev_qualification[0],
        'Previous_qualification_grade': prev_grade,
        'Nacionality': nationality[0],
        'Mothers_qualification': mothers_qual[0],
        'Fathers_qualification': fathers_qual[0],
        'Mothers_occupation': mothers_occ[0],
        'Fathers_occupation': fathers_occ[0],
        'Admission_grade': admission_grade,
        'Displaced': displaced[1],
        'Educational_special_needs': special_needs[1],
        'Debtor': int(debtor),
        'Tuition_fees_up_to_date': int(tuition_fees),
        'Gender': gender[1],
        'Scholarship_holder': int(scholarship),
        'Age_at_enrollment': age,
        'International': international[1],
        'Curricular_units_1st_sem_credited': cu_1st_credited,
        'Curricular_units_1st_sem_enrolled': cu_1st_enrolled,
        'Curricular_units_1st_sem_evaluations': cu_1st_evaluations,
        'Curricular_units_1st_sem_approved': cu_1st_approved,
        'Curricular_units_1st_sem_grade': cu_1st_grade,
        'Curricular_units_1st_sem_without_evaluations': cu_1st_wo_evaluations,
        'Curricular_units_2nd_sem_credited': cu_2nd_credited,
        'Curricular_units_2nd_sem_enrolled': cu_2nd_enrolled,
        'Curricular_units_2nd_sem_evaluations': cu_2nd_evaluations,
        'Curricular_units_2nd_sem_approved': cu_2nd_approved,
        'Curricular_units_2nd_sem_grade': cu_2nd_grade,
        'Curricular_units_2nd_sem_without_evaluations': cu_2st_wo_evaluations,
        'Unemployment_rate': unemployment,
        'Inflation_rate': inflation,
        'GDP': gdp
    }
    
    input_df = pd.DataFrame([input_data])
    
    try:
        prediction = model.predict(input_df)[0]
        
        st.subheader("Prediction Results")
        
        if prediction == 0:
            st.error(f"Student Status : Dropout")
        else:
            st.success(f"Student Status : Not Dropout")
        
    
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        st.write("Please check that all inputs are correctly filled.")