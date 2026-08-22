from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.rbac import router as rbac_router

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

app.include_router(auth_router)
app.include_router(rbac_router)

    
    
