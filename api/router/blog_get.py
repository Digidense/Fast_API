from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get('/hello')
def index():
    return {'message': 'hello world!'}

@router.get('/blog/all')
def get_all_blogs():
    return {'message': 'All blogs provided'}

#quary parameter
@router.get('/blog/{id}/comments/{comments_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


class BlogeType(str, Enum):
    short = 'short'
    story = 'sory'
    howto = 'howto'

@router.get('/blog/type/{type}')
def get_blog_type(type: BlogeType):
    return {'message': f'Blog type {type}'}

#ststus code and Tages
# tage is tages = ['blog']

@router.get('/blog/{id}',status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
    
#summery and description

@router.get('/test', 
         tags=['summery'],
         summary='testing purpose',
         description='all ok',
         response_description='the list of avaliable')
def summery():
    return {'message': 'hello world!'}