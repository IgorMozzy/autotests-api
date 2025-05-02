import json
from functools import wraps

import httpx


API_BASE_URL = "http://localhost:8000/api/v1"
AUTH_ENDPOINT = f"{API_BASE_URL}/authentication/login"
USER_INFO_ENDPOINT = f"{API_BASE_URL}/users/me"

USER_EMAIL = "a@a.ru"
USER_PASSWORD = "password"

client = httpx.Client()

def log_response_to_console(func):
    """Декоратор для логирования HTTP-ответов в консоль"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        response: httpx.Response = func(*args, **kwargs)
        print(f"\n[Response from: {func.__name__}]")
        print("Docstring:", func.__doc__)
        print("Request URL:", response.url)
        print("Status Code:", response.status_code)
        try:
            data = response.json()
            print("Response JSON:", json.dumps(data, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print("Raw Response Text:", response.text)
        return response
    return wrapper

@log_response_to_console
def get_access_token(httpx_client: httpx.Client, login: str, password: str) -> httpx.Response:
    """Получение access токена"""
    login_payload = {
        "email": login,
        "password": password
    }
    return httpx_client.post(AUTH_ENDPOINT, json=login_payload)

@log_response_to_console
def get_user_me(httpx_client: httpx.Client, auth_token: str) -> httpx.Response:
    """Получение информации о владельце токена"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    return httpx_client.get(USER_INFO_ENDPOINT, headers=headers)


if __name__ == "__main__":
    login_response = get_access_token(client, USER_EMAIL, USER_PASSWORD)
    try:
        access_token = login_response.json()["token"]["accessToken"]
        get_user_me(client, access_token)
    except (KeyError, TypeError, ValueError):
        print("Ошибка при получении токена")

