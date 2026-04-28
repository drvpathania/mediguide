from pydantic import BaseModel


class PatientCreate(BaseModel):
    name: str
    age: int
    symptoms: str


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    symptoms: str

    class Config:
        from_attributes = True