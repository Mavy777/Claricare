from pydantic import BaseModel

class Vitals(BaseModel):
    heart_rate: int
    blood_pressure_systolic: int
    blood_pressure_diastolic: int
    respiratory_rate: int
    spo2: int
    temperature_celsius: float
