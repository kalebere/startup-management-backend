from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ...schema import Prompt
from ...core import LLMChain

router = APIRouter()


@router.post("/generator")
def idea_generator(user_prompt : Prompt):
    response = LLMChain.main_run(user_prompt.prompt)

    return JSONResponse({"Response":response})