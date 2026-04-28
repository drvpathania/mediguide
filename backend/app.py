from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import os
import json

from backend.database import SessionLocal, engine, Base
from backend.models import Patient
from backend.schemas import PatientCreate, PatientResponse

# Create DB tables
Base.metadata.create_all(bind=engine)

# -------- AI SETUP --------
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    AI_ENABLED = True
except Exception as e:
    print("AI disabled:", e)
    AI_ENABLED = False

app = FastAPI()

# -------- CORS --------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- DB DEP --------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- ROOT --------
@app.get("/")
def root():
    return {"message": "Mediguide API running 🚀"}

# -------- CREATE PATIENT --------
@app.post("/patients", response_model=PatientResponse)
def create_patient(data: PatientCreate, db: Session = Depends(get_db)):
    patient = Patient(**data.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

# -------- GET PATIENTS --------
@app.get("/patients")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

# -------- AI ANALYZE --------
@app.post("/analyze")
def analyze(data: PatientCreate):

    fallback = {
        "diagnosis": "General ENT Issue",
        "differentials": ["Otitis externa", "CSOM", "Fungal infection"],
        "advice": "Consult ENT specialist",
        "treatment": "Clinical examination required",
        "urgency": "Medium"
    }

    if AI_ENABLED:
        try:
            prompt = f"""
You are an experienced ENT specialist.

Patient:
Name: {data.name}
Age: {data.age}
Symptoms: {data.symptoms}

Respond ONLY in JSON:
{{
  "diagnosis": "...",
  "differentials": ["...", "..."],
  "advice": "...",
  "treatment": "...",
  "urgency": "Low/Medium/High"
}}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            content = response.choices[0].message.content.strip()
            content = content.replace("```json", "").replace("```", "")

            ai_output = json.loads(content)

            return {**fallback, **ai_output}

        except Exception as e:
            print("AI error:", e)

    return fallback