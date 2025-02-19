from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load API Key from .env
client = OpenAI(
  api_key="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"
)
app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeRequest(BaseModel):
    job_description: str
    resume_bullet: str

@app.post("/optimize_bullet")
async def optimize_bullet(request: ResumeRequest):
    prompt = f"Improve this resume bullet point based on the following job description:\n\nJob Description: {request.job_description}\nResume Bullet: {request.resume_bullet}\n\nOptimized Resume Bullet:"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert resume writer."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"optimized_bullet": response.choices[0].message.content}
    
    except Exception as e:
        return {"error": str(e)}
