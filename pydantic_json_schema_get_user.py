from api_client_get_user import private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema, UserSchema, \
    CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
# Создание и получение объекта пользователя
create_user_response = public_users_client.create_user_api(create_user_request)
# Получаем JSON схему из модели ответа
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
# Проверяем, что JSON ответ от API соответствует ожидаемой JSON схеме
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)
# Получаем объект пользователя из модели ответа
parsed_response = CreateUserResponseSchema.model_validate(create_user_response.json())
user = parsed_response.user

# Получение информации о пользователе
user_request = private_users_client.get_user_api(user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
# Проверяем, что JSON ответ от API соответствует ожидаемой JSON схеме
validate_json_schema(instance=user_request.json(), schema=get_user_response_schema)
