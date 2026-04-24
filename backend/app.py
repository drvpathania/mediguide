from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ Allow frontend (Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- MODEL --------
class PatientInput(BaseModel):
    name: str
    age: int
    symptoms: str


# -------- ROUTES --------
@app.get("/")
def read_root():
    return {"message": "Mediguide API running 🚀"}


@app.post("/analyze")
def analyze(data: PatientInput):
    symptoms = data.symptoms.lower()

    if "ear pain" in symptoms:
        diagnosis = "Possible Ear Infection (Otitis)"
        advice = "Avoid water entry, may need ear drops"
        urgency = "Medium"

    elif "snoring" in symptoms:
        diagnosis = "Possible Sleep Apnea"
        advice = "Sleep study recommended"
        urgency = "High"

    elif "throat pain" in symptoms:
        diagnosis = "Tonsillitis / Pharyngitis"
        advice = "Warm saline gargles, ENT consult"
        urgency = "Low"

    else:
        diagnosis = "General ENT Issue"
        advice = "Consult ENT specialist"
        urgency = "Medium"

    return {
        "patient": data.name,
        "diagnosis": diagnosis,
        "advice": advice,
        "urgency": urgency
    }