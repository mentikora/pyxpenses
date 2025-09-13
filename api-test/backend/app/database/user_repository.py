from peewee import AutoField, CharField, IntegerField, Model

from ..models.users import UserBaseSchema, UserSchema
from .database import db


class UserModel(Model):
    id = AutoField()
    first_name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    email = CharField(unique=True)
    age = IntegerField()
    status = CharField()
    gender = CharField()

    class Meta:
        database = db
        table_name = "users"


class UserRepository:
    """
    Repository class for handling User database operations
    """

    def __init__(self, db):
        """
        Initialize the UserRepository with database connection

        Args:
            db: The database connection object
        """
        self.db = db

    def get_all(self, skip: int, limit: int) -> list[UserSchema]:
        """
        Fetch all users from the database.add()

        Args:
            skip (int): ...
            limit (int): ...

        Returns:
            list[UserSchema]: A list of user schemas representing all users in the database.
        """
        query = self.db.select().offset(skip).limit(limit)

        return [UserSchema.model_validate(user.__data__) for user in query]

    def create_user(self, user: UserBaseSchema):
        """
        Create a new user in the database

        Args:
            user (UserSchema): The user shema containing user data

        Returns:
            UserModel: The created user model instance
        """
        return self.db.create(**user.model_dump())
