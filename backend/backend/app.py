from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

# OPTIONAL AI (safe import)
try:
    from openai import OpenAI
    import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    AI_ENABLED = True
except:
    AI_ENABLED = False

app = FastAPI()

# ✅ CORS (VERY IMPORTANT for Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# REQUEST MODEL
# -------------------------------
class PatientInput(BaseModel):
    name: str
    age: int
    symptoms: str


# -------------------------------
# ROOT
# -------------------------------
@app.get("/")
def read_root():
    return {"message": "Mediguide API running 🚀"}


# -------------------------------
# ANALYZE (MAIN API)
# -------------------------------
@app.post("/analyze")
def analyze(data: PatientInput):

    symptoms = data.symptoms.lower()

    # ----------------------------------
    # 🔵 RULE-BASED FALLBACK (ALWAYS SAFE)
    # ----------------------------------
    diagnosis = "General ENT Issue"
    advice = "Consult ENT specialist"
    urgency = "Low"

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

    # ----------------------------------
    # 🟣 AI ENHANCEMENT (if available)
    # ----------------------------------
    if AI_ENABLED:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an ENT specialist. Give diagnosis, advice, and urgency (Low/Medium/High)."
                    },
                    {
                        "role": "user",
                        "content": f"Patient: {data.name}, Age: {data.age}, Symptoms: {data.symptoms}"
                    }
                ],
            )

            ai_text = response.choices[0].message.content

            # simple override (optional)
            diagnosis = "AI Suggestion"
            advice = ai_text
            urgency = "Consult Doctor"

        except Exception as e:
            print("AI failed, using fallback:", e)

    # ----------------------------------
    # RESPONSE
    # ----------------------------------
    return {
        "diagnosis": diagnosis,
        "advice": advice,
        "urgency": urgency
    }