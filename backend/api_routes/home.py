from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["root"])
async def route():
    return {"data", "hello from FastAPI"}


