import requests
from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, description="get all characters")
def get_avatar():
    try:
        url = "https://last-airbender-api.fly.dev/api/v1/characters"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
