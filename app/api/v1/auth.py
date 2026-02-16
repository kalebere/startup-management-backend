from fastapi import APIRouter, status
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import timedelta

from ...schema import Login as Login_schema
from ...schema import authentication as auth_token_schema
from ...database import auth_collection
from ...auth import verify_password,create_access_token,verify_access_token

router = APIRouter()

@router.post("/login")
def login(user:Login_schema):

    res = auth_collection.find_one(
        {"username" : user.username}
    )

    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found!")

    login = verify_password(user.password,res.get("password",""))

    if not login:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not Authorized")
    
    jwt_token = create_access_token({"username":user.username},timedelta(minutes=15))
    
    return JSONResponse({"Success": True,"token":jwt_token},status_code=status.HTTP_200_OK)

@router.post("/protected")
def protected(token_data : auth_token_schema):
    payload = verify_access_token(token_data.token)

    if not payload:
        raise HTTPException(detail="Logged Out!",status_code=status.HTTP_401_UNAUTHORIZED)
    
    return JSONResponse({"username": payload.get("username")})
