import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_vitals(vitals):
    prompt = f"""
    Patient's vitals:
    - Heart rate: {vitals.heart_rate} bpm
    - Blood pressure: {vitals.blood_pressure_systolic}/{vitals.blood_pressure_diastolic} mmHg
    - Respiratory rate: {vitals.respiratory_rate} breaths/min
    - SpO2: {vitals.spo2}%
    - Temperature: {vitals.temperature_celsius}°C

    Please provide a clear explanation of what these vitals mean for a concerned family member with no medical background. Mention any values that are above or below normal and what might cause them.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message['content']
