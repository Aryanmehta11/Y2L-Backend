from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from utils.transcript import get_transcript
from utils.summarizer import generate_linkedin_post  # ✅ FIXED import

app = FastAPI()

# 👇 Add this block to enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "YouTube to LinkedIn Backend is Running!"}

@app.get("/generate-post/")
def generate_post(video_id: str = Query(..., description="YouTube Video ID")):
    transcript = get_transcript(video_id)
    if transcript.startswith("Error:"):
        raise HTTPException(status_code=400, detail=transcript)

    result = generate_linkedin_post(transcript)
    if result.get("error"):
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # returns both "post" and "bullet_points"
