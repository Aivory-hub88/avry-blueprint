"""
avry-blueprint Microservice Entry Point
Description: AI blueprint generation
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="AVRY Blueprint Service",
    description="AI blueprint generation",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include routes
try:
    from app.routes.blueprint import router as blueprint_router
    app.include_router(blueprint_router)
    print("[✓] Blueprint routes registered")
except Exception as e:
    print(f"[!] Warning: Could not import blueprint routes: {e}")
try:
    from app.routes import *
    # Include routers here as needed
except Exception as e:
    print(f"Warning: Could not import routes: {e}")

# Health check endpoint
@app.get("/health")
async def health():
    """Service health check"""
    return {
        "status": "healthy",
        "service": "avry-blueprint",
        "version": "1.0.0"
    }

@app.get("/")
async def root():
    """Service info"""
    return {
        "service": "AVRY Blueprint Service",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8083"))
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        reload=os.getenv("ENVIRONMENT", "production") == "development"
    )
