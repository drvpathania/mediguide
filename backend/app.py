from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mediguide running 🚀"}


@app.post("/ai-consult")
def ai_consult(symptoms: str):
    return {
        "diagnosis": f"Based on '{symptoms}', likely ENT/Eye/Skin issue.",
        "advice": "Consult specialist if symptoms persist"
    }