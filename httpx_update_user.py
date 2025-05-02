import httpx
from tools.fakers import get_fake_user_payload


API_BASE_URL = "http://localhost:8000/api/v1"
AUTH_ENDPOINT = f"{API_BASE_URL}/authentication/login"
USERS_ENDPOINT = f"{API_BASE_URL}/users"


# Создаем нового пользователя
new_user_payload = get_fake_user_payload()
create_user_response = httpx.post(USERS_ENDPOINT, json=new_user_payload)
create_user_response_data = create_user_response.json()
print('Create user status code:', create_user_response.status_code)
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": new_user_payload['email'],
    "password": new_user_payload['password']
}
login_response = httpx.post(AUTH_ENDPOINT, json=login_payload)
login_response_data = login_response.json()
print('Login status code:', login_response.status_code)
print('Login data:', login_response_data)

# Обновление данных пользователя
update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
update_user_payload = get_fake_user_payload()
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=update_user_headers, json=update_user_payload
)
print('Update user status code:', update_user_response.status_code)
print('Updated user data:', update_user_response.json())
