import json
from pytest import mark

from fastapi.security import OAuth2PasswordRequestForm


@mark.users
class TestUsers():
    collection = 'users'

    def compare_response_and_test_users(self, response, test_admin_or_user):
        response_fields_remove = ['id', 'image']
        test_fields_remove = ['password', 'password_confirm']

        response_user = dict(response.json())
        response_user = {k: v for k, v in response_user.items() if k not in response_fields_remove}
        test_admin_or_user = {k: v for k, v in test_admin_or_user.items()
                              if not k.startswith('password')}
        return response_user == test_admin_or_user

    def signup(self, test_client, test_admin_or_user):
        return test_client.post(f"/{self.collection}/signup", data=test_admin_or_user)

    def login(self, test_client, test_login_admin_or_user):
        return test_client.post(f"/{self.collection}/login", data=test_login_admin_or_user)

    def get_token(self, test_client, test_admin_or_user, test_login_admin_or_user):
        self.signup(test_client, test_admin_or_user)
        response = self.login(test_client, test_login_admin_or_user)
        return response.json()['access_token']

    def test_admin_get_users(self, test_client, test_admin, test_login_admin):
        token = self.get_token(test_client, test_admin, test_login_admin)
        response = test_client.get(f"/{self.collection}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_user_get_users(self, test_client, test_user, test_login_user):
        token = self.get_token(test_client, test_user, test_login_user)
        response = test_client.get(f"/{self.collection}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 401
        assert response.json()['detail'] == 'Credenciales invalidas'

    def test_post_user(self, test_client, test_user):
        response = self.signup(test_client, test_user)
        assert response.status_code == 201

    def test_post_user_with_diferent_passwords(self, test_client, test_user):
        test_user['password_confirm'] = 'diferent_password'
        response = self.signup(test_client, test_user)
        assert response.status_code == 400
        assert response.json()['detail'] == "Los passwords no coinciden"

    def test_post_existing_user(self, test_client, test_user):
        self.signup(test_client, test_user)
        response = self.signup(test_client, test_user)
        assert response.status_code == 409
        assert response.json()['detail'] == 'El usuario ya existe'

    def test_login_existing_active_user(self, test_client, test_user, test_login_user):
        self.signup(test_client, test_user)
        response = self.login(test_client, test_login_user)
        assert response.status_code == 200
        assert 'access_token' in response.json()

    def test_login_existing_inactive_user(self, test_client, test_user, test_login_user):
        test_user['is_active'] = False
        self.signup(test_client, test_user)
        response = self.login(test_client, test_login_user)
        assert response.status_code == 400
        assert response.json()['detail'] == 'Usuario inactivo o eliminado'

    def test_login_not_existing_user(self, test_client, test_login_user):
        response = self.login(test_client, test_login_user)
        assert response.status_code == 403
        assert response.json()['detail'] == 'Usuario o contraseña incorrecta'

    def test_get_user_me(self, test_client, test_user, test_login_user):
        token = self.get_token(test_client, test_user, test_login_user)
        response = test_client.get(f"/{self.collection}/me",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 200
        assert self.compare_response_and_test_users(response, test_user)

    def test_get_user_me_without_auth(self, test_client):
        response = test_client.get(f"/{self.collection}/me")
        assert response.status_code == 401
        assert response.json()['detail'] == "Usuario no autenticado"

    def test_get_user_me_wrong_token(self, test_client):
        token = 'wrong token'
        response = test_client.get(f"/{self.collection}/me",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 401
        assert response.json()['detail'] == 'Credenciales invalidas'

    def test_admin_get_existing_user(self, test_client, test_admin, test_user, test_login_admin):
        token = self.get_token(test_client, test_admin, test_login_admin)
        response = self.signup(test_client, test_user)
        id = response.json()['id']

        response = test_client.get(f"/{self.collection}/{id}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 200
        assert self.compare_response_and_test_users(response, test_user)

    def test_unauthorized_get_existing_user(self, test_client, test_user):
        token = 'fake token'
        response = self.signup(test_client, test_user)
        id = response.json()['id']

        response = test_client.get(f"/{self.collection}/{id}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 401
        assert response.json()['detail'] == 'Credenciales invalidas'

    def test_fail_get_not_existing_user(self, test_client, test_admin, test_login_admin):
        token = self.get_token(test_client, test_admin, test_login_admin)
        id = '645b4d9e5f81141374088b6c'
        response = test_client.get(f"/{self.collection}/{id}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 400
        assert response.json()['detail'] == 'La instancia no existe'

    def test_fail_get_not_valid_id(self, test_client, test_admin, test_login_admin):
        token = self.get_token(test_client, test_admin, test_login_admin)
        id = 'invalid id'
        response = test_client.get(f"/{self.collection}/{id}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 400

        expected_msg = 'invalid id no es un ObjectId válido, debe ser un input' \
            + ' (12-byte) o una cadena hexadecimal (24-character)'
        print(response.json()['detail'], expected_msg)
        assert response.json()['detail'] == expected_msg

    # def test_delete_user(self, test_client, test_user, test_image):
    #     response = test_client.post(f"/{self.collection}",
    #                                 files=test_image,
    #                                 data=test_user)
    #     id = response.json()['id']
    #     assert len(test_client.get(f"/{self.collection}").json()) == 1

    #     response = test_client.delete(f"/{self.collection}/{id}")
    #     assert response.status_code == 204

    #     assert len(test_client.get(f"/{self.collection}").json()) == 0

    # def test_update_user(self, test_client, test_user, test_user_updated, test_image):
    #     response = test_client.post(f"/{self.collection}",
    #                                 files=test_image,
    #                                 data=test_user)
    #     id = response.json()['id']
    #     response = test_client.put(f"/{self.collection}/{id}",
    #                                content=json.dumps(test_user_updated))
    #     assert response.status_code == 200

    #     updated_db_user = test_client.get(f"/{self.collection}/{id}").json()
    #     test_user_updated['id'] = id
    #     assert updated_db_user == test_user_updated
