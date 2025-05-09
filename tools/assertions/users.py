from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что переданные в функцию модели пользователей совпадают.

    :param actual: Фактическая модель пользователя.
    :param expected: Ожидаемая модель пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


def assert_get_user_response(create_user_response: CreateUserResponseSchema, get_user_response: GetUserResponseSchema):
    """
    Проверяет, что ответ на получение данных пользователя возвращает данные созданного пользователя.

    :param create_user_response: Ответ API с данными созданного пользователя.
    :param get_user_response: Ответ API с данными пользователя-владельца access-токена созданного пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_user(get_user_response.user, create_user_response.user)
