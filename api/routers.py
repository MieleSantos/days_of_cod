from fastapi import APIRouter

from api.controllers.avatar import router as avatar

router = APIRouter()
router.include_router(avatar, prefix='/avatar', tags=['Avatar'])
