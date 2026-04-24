from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to Netlify URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root test
@app.get("/")
def read_root():
    return {"message": "Backend is running"}

# ✅ Login API
@app.post("/login")
def login():
    return {"message": "Login successful 🚀"}