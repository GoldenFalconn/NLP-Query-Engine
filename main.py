from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Import routes
from .routes import schema, ingestion, query

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="NLP Query Engine API",
    description="Natural Language Query System for Employee Database",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(schema.router)
app.include_router(ingestion.router)
app.include_router(query.router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "NLP Query Engine API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "NLP Query Engine"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
