from fastapi import APIRouter
from ...schema import Prompt

router = APIRouter()


@router.post("/generator")
def idea_generator(user_prompt : Prompt):
    ...