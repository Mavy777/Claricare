from fastapi import FastAPI
from vitals_schema import Vitals
from explainer import explain_vitals

app = FastAPI()

@app.post("/explain")
def get_explanation(vitals: Vitals):
    explanation = explain_vitals(vitals)
    return {"explanation": explanation}
