import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")

st.set_page_config(page_title="ClariCare Vitals Explainer", layout="centered")
st.title("🩺 ClariCare - Vitals Explainer")

st.markdown("Enter the patient's vitals below to receive an easy-to-understand explanation.")

with st.form("vitals_form"):
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=0, value=75)
    systolic = st.number_input("Systolic BP (mmHg)", min_value=0, value=120)
    diastolic = st.number_input("Diastolic BP (mmHg)", min_value=0, value=80)
    respiratory_rate = st.number_input("Respiratory Rate (breaths/min)", min_value=0, value=16)
    spo2 = st.number_input("SpO2 (%)", min_value=0, max_value=100, value=98)
    temperature = st.number_input("Temperature (°C)", min_value=25.0, max_value=45.0, value=37.0)

    submitted = st.form_submit_button("Explain Vitals")

if submitted:
    data = {
        "heart_rate": heart_rate,
        "blood_pressure_systolic": systolic,
        "blood_pressure_diastolic": diastolic,
        "respiratory_rate": respiratory_rate,
        "spo2": spo2,
        "temperature_celsius": temperature
    }

    with st.spinner("🧠 Generating explanation..."):
        try:
            response = requests.post(API_URL, json=data)
            response.raise_for_status()
            explanation = response.json()["explanation"]
            st.success("Explanation generated!")
            st.markdown(f"### 💬 Explanation
{explanation}")
        except Exception as e:
            st.error(f"Error: {e}")
