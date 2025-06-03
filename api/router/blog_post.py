from fastapi import APIRouter

router = APIRouter(
    prefix='/blog',
    tags=['bloge']
)

@router.post('/')
def create_blog():
    pass