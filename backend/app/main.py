from fastapi import FastAPI

app = FastAPI(
    title="SmartAttend AI",
    description="AI-based Face Recognition Attendance System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "SmartAttend AI Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
