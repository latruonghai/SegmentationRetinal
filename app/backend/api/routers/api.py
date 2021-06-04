from fastapi import APIRouter
from . import images, retrieval

router = APIRouter()
router.include_router(images.router, tags=["Images"])
router.include_router(retrieval.router, tags=["IR"])

@router.get("/")
async def hello_world():
    return {"title": "Hello",
            "body": "What's up"}