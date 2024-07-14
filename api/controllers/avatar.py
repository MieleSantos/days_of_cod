import requests
from fastapi import APIRouter, HTTPException, status, Query
from googletrans import Translator

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, description="get all characters")
def get_avatar():
    try:
        url = "https://last-airbender-api.fly.dev/api/v1/characters"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get(
    "/tradutor", status_code=status.HTTP_200_OK, description="get all characters"
)
def get_tradutor(
    name: str = Query(description="Name"),
    affiliation: str = Query(description="affiliation"),
):
    tradutor = Translator()

    resp = tradutor.translate(src="en", dest="pt", text=name)
    affil = tradutor.translate(src="en", dest="pt", text=affiliation)

    return {
        "name": {"origin": resp.origin, "taducao": resp.text},
        "affiliation": {"origin": affil.origin, "taducao": affil.text},
    }
