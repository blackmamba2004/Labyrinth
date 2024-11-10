from fastapi import APIRouter, Security, Request

from backend.pkg.auth.middlewares.jwt.service import check_access_token


router = APIRouter(prefix='/users', tags=['Users'])


@router.get(path='/me', dependencies=[Security(check_access_token)])
async def get_me_user_info(request: Request):
    return f'Hello, {request.state.user.email}'