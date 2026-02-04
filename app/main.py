# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agents.diagnosis_agent import DiagnosisAgent

app = FastAPI(title="Medical Diagnosis AI API")
agent = DiagnosisAgent()

# Define what the incoming data should look like
class PatientRequest(BaseModel):
    symptoms_text: str

@app.get("/")
def read_root():
    return {"status": "Online", "message": "Medical AI Agent is ready."}

@app.post("/diagnose")
async def diagnose_patient(request: PatientRequest):
    try:
        # Run the agent logic
        report = agent.run(request.symptoms_text)
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)