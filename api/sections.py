import fastapi

router = fastapi.APIRouter()


@router.get("/sections/{id}")
async def get_sections():
    return {"courses": []}

@router.get("/sections/{id}/content")
async def section_content():
    return {"courses": []}