import uuid

from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class UserBase(BaseModel):
    """
    Шаблон модели пользователя с базовыми публичными полями.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class UserSchema(UserBase):
    """
    Базовая схема пользователя.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))


class CreateUserRequestSchema(UserBase):
    """
    Схема запроса создания пользователя.
    """
    password: str

class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания пользователя.
    """
    user: UserSchema

incoming_data = {
    "email": "email@example.com",
    "firstName": "John",
    "lastName": "Doe",
    "middleName": "Junior",
    "password": "password123"
}


# Инициализация CreateUserRequestSchema
create_user_request = CreateUserRequestSchema(**incoming_data)
print(f"Parsed CreateUserRequestSchema: {create_user_request}")

# Сериализация CreateUserRequestSchema в camelCase JSON
create_user_request_json = create_user_request.model_dump_json(by_alias=True)
print(f"CreateUserRequestSchema serialized to JSON: {create_user_request_json}")

# Инициализация UserSchema
_ = incoming_data.pop("password")
user_schema = UserSchema(**incoming_data)
print(f"Parsed UserSchema: {user_schema}")

# Сериализация UserSchema в camelCase JSON
user_schema_json = user_schema.model_dump_json(by_alias=True)
print(f"Serialized UserSchema: {user_schema_json}")

# Инициализация CreateUserResponseSchema
create_user_response = CreateUserResponseSchema(user=user_schema)
print(f"CreateUserResponseSchema: {create_user_response}")
