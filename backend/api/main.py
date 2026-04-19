import modal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app_image = modal.Image.debian_slim().pip_install(
    "fastapi", "uvicorn", "python-multipart"
)

app = modal.App("spatialphysics-api")
web_app = FastAPI(title="SpatialPhysics API")

web_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@web_app.get("/health")
async def health():
    return {"status": "ok", "service": "spatialphysics-api"}

@web_app.get("/")
async def root():
    return {"message": "SpatialPhysics AI - Phase 1"}

@app.function(image=app_image)
@modal.asgi_app()
def fastapi_app():
    return web_app