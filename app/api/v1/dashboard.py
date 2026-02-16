from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ...schema import Prompt
from ...core import LLMChain
from ...auth import get_current_user

router = APIRouter()

from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "MY_SUPER_SECRET_KEY"
ALGORITHM = "HS256"

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        return username

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired or invalid"
        )

import re

def clean_markdown(text: str) -> str:
    """Remove markdown symbols and format nicely"""

    # remove headings ###, **, ---
    text = re.sub(r'#+\s*', '', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'---', '', text)

    # convert bullets * into •
    text = re.sub(r'^\s*\*\s*', '• ', text, flags=re.MULTILINE)

    # remove extra blank lines
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return text.strip()


def parse_ai_response(text: str):
    roadmap_match = re.search(r"### 1[\s\S]*?(?=### 2)", text)
    skills_match = re.search(r"### 2[\s\S]*?(?=### 3)", text)
    budget_match = re.search(r"### 3[\s\S]*", text)

    roadmap = clean_markdown(roadmap_match.group(0)) if roadmap_match else ""
    skills = clean_markdown(skills_match.group(0)) if skills_match else ""
    budget = clean_markdown(budget_match.group(0)) if budget_match else ""

    return roadmap, skills, budget

@router.post("/generator")
def idea_generator(user_prompt : Prompt):
    response = LLMChain.main_run(user_prompt.prompt)
    roadmap, skills, budget = parse_ai_response(response)

    return JSONResponse(
        {
            "roadmap":roadmap,
            "skills":skills,
            "budget":budget

        }
    )