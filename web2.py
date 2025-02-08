import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


parkinsons_model_path = os.path.join(BASE_DIR, "training-models", "parkinson_model.sav")
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

# Load Models
#diabetes_model = pickle.load(open(r"C:\Users\ASUS\OneDrive\Documents\disease-outbreak\training-models\diabetes_model.sav", 'rb'))
#heart_model = pickle.load(open(r"C:\Users\ASUS\OneDrive\Documents\disease-outbreak\training-models\heart_model.sav", 'rb'))
#parkinsons_model = pickle.load(open(r"C:\Users\ASUS\OneDrive\Documents\disease-outbreak\training-models\parkinson_model.sav", 'rb'))
diabetes_model_path = os.path.join(BASE_DIR, "training-models", "diabetes_model.sav")
heart_model_path = os.path.join(BASE_DIR, "training-models", "heart_model.sav")
parkinsons_model_path = os.path.join(BASE_DIR, "training-models", "parkinson_model.sav")


# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreak System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction'],
        menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Clear existing elements to prevent overlap
placeholder = st.empty()

# ---------- DIABETES PREDICTION ----------
if selected == 'Diabetes Prediction':
    with placeholder.container():
        st.title('Diabetes Prediction using ML')
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
            SkinThickness = st.text_input('Skin Thickness value')
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Glucose = st.text_input('Glucose Level')
            Insulin = st.text_input('Insulin Level')
            Age = st.text_input('Age of the Person')

        with col3:
            Bloodpressure = st.text_input('Blood Pressure Value')
            BMI = st.text_input('BMI Value')

        if st.button('Diabetes Test Result'):
            user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])
            result = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(result)

# ---------- HEART DISEASE PREDICTION ----------
elif selected == 'Heart Disease Prediction':
    with placeholder.container():
        st.title('Heart Disease Prediction using ML')
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')
            trestbps = st.text_input('Trestbps')
            thalach = st.text_input('Thalach')
            oldpeak = st.text_input('Oldpeak')
            thal = st.text_input('Thal')

        with col2:
            sex = st.text_input('Sex (Female=0, Male=1)')
            chol = st.text_input('Cholesterol Level')
            exang = st.text_input('Exang')
            slope = st.text_input('Slope')

        with col3:
            cp = st.text_input('Chest Pain Type')
            restecg = st.text_input('Restecg')
            ca = st.text_input('Ca')
            fbs = st.text_input('Fbs')

        if st.button('Heart Disease Test Result'):
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_model.predict([user_input])
            result = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
            st.success(result)

# ---------- PARKINSON'S DISEASE PREDICTION ----------
elif selected == 'Parkinsons Disease Prediction':
    with placeholder.container():
        st.title("Parkinson's Disease Prediction using ML")
        col1, col2, col3 = st.columns(3)

        with col1:
            PPE = st.text_input('PPE')
            MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
            MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
            MDVP_Flo = st.text_input('MDVP:Flo')
            MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
            MDVP_RAP = st.text_input('MDVP:RAP')
            Jitter_DDP = st.text_input('Jitter:DDP')
            NHR= st.text_input('NHR')

        with col2:
            MDVP_JitterAbs = st.text_input('MDVP:Jitter(Abs)')
            MDVP_PPQ = st.text_input('MDVP:PPQ')
            MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
            MDVP_APQ = st.text_input('MDVP:APQ')
            Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
            Shimmer_DDA = st.text_input('Shimmer:DDA')
            MDVP_shimmer = st.text_input('MDVP shimmer')


        with col3:
            Shimmer_APQ5 = st.text_input('Shimmer_APQ5')
            RPDE = st.text_input('RPDE')
            DFA = st.text_input('DFA')
            spread1 = st.text_input('Spread1')
            spread2 = st.text_input('Spread2')
            D2 = st.text_input('D2')
            HNR=st.text_input('HNR')

        if st.button("Parkinson's Disease Test Result"):
            
            user_input=[  PPE,
            MDVP_Fo ,
            MDVP_Fhi ,
            MDVP_Flo ,
            MDVP_Jitter ,
            MDVP_RAP ,
            Jitter_DDP,
            NHR,
            MDVP_shimmer,
            MDVP_JitterAbs ,
            MDVP_PPQ ,
            MDVP_Shimmer_dB ,
            MDVP_APQ ,
            Shimmer_APQ3 ,
            Shimmer_DDA ,

       
            Shimmer_APQ5 ,
            HNR ,
            RPDE,
            DFA,
            spread1,
            spread2 ,
            D2 ]
            user_input = [float(x) for x in user_input]
            parkinson_prediction = parkinsons_model.predict([user_input])
            result = "The person has Parkinson's disease" if parkinson_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(result)
