from fastapi import APIRouter
from ..models.users import UserSchema, UserBaseSchema
from ..database.user_repository import UserRepository
from ..database.user_repository import UserModel

user_repo = UserRepository(UserModel)

router = APIRouter(
    prefix='/users',
    tags=['Users'],
    responses={
        '404': { 'description': 'Not found' },
    }
)

@router.get('/')
def get_users(skip: int = 0, limit: int = 10) -> list[UserSchema]:
    return user_repo.get_all(skip, limit)


@router.get('/{id}')
def get_user(id: int) -> UserSchema:
    pass


@router.post('/')
def post_user(user: UserBaseSchema):
    return user_repo.create_user(user)


@router.put('/{id}')
def put_user(id: int):
    pass


@router.patch('/{id}')
def patch_user(id: int):
    pass


@router.delete('/{id}')
def delete_user(id: int):
    pass