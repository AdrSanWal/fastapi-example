from pytest import mark

from backend.api.auth.utils import authenticated_user
from api import error_msg


@mark.users
class TestUsers():
    collection = 'users'

    def compare_response_and_test_users(self, response, test_admin_or_user):
        response_fields_remove = ['id', 'image']

        response_user = dict(response.json())
        test_admin_or_user = test_admin_or_user['user']
        response_user = {k: v for k, v in response_user.items() if k not in response_fields_remove}
        test_admin_or_user = {k: v for k, v in test_admin_or_user.items()
                              if not k.startswith('password')}
        return response_user == test_admin_or_user

    def signup(self, test_client, test_admin_or_user):
        return test_client.post(f"/{self.collection}/signup",
                                data=test_admin_or_user['user'])

    def login(self, test_client, test_admin_or_user):
        return test_client.post(f"/{self.collection}/login",
                                data=test_admin_or_user['login'])

    def get_token(self, test_client, test_admin_or_user):
        self.signup(test_client, test_admin_or_user)
        response = self.login(test_client, test_admin_or_user)
        return response.json()['access_token']

    # ------------------------------------------------------------#
    # ---------------------------TESTS--------------------------- #
    # ------------------------------------------------------------#

    def test_admin_get_users(self, test_client, test_admin):
        token = self.get_token(test_client, test_admin)
        response = test_client.get(f"/{self.collection}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_user_get_users(self, test_client, test_user):
        token = self.get_token(test_client, test_user)
        response = test_client.get(f"/{self.collection}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 401
        assert response.json()['detail'] == error_msg.invalid_credentials

    def test_post_user(self, test_client, test_user):
        response = self.signup(test_client, test_user)
        assert response.status_code == 201

    def test_post_user_with_diferent_passwords(self, test_client, test_user):
        test_user['user']['password_confirm'] = 'diferent_password'
        response = self.signup(test_client, test_user)
        assert response.status_code == 400
        assert response.json()['detail'] == error_msg.diferent_passwords

    def test_post_existing_user(self, test_client, test_user):
        self.signup(test_client, test_user)
        response = self.signup(test_client, test_user)
        assert response.status_code == 409
        assert response.json()['detail'] == error_msg.user_already_exists

    def test_login_existing_active_user(self, test_client, test_user):
        self.signup(test_client, test_user)
        response = self.login(test_client, test_user)
        assert response.status_code == 200
        assert 'access_token' in response.json()

    def test_login_existing_inactive_user(self, test_client, test_user):
        test_user['user']['is_active'] = False
        self.signup(test_client, test_user)
        response = self.login(test_client, test_user)
        assert response.status_code == 400
        assert response.json()['detail'] == error_msg.user_inactive

    def test_login_not_existing_user(self, test_client, test_user):
        response = self.login(test_client, test_user)
        assert response.status_code == 403
        assert response.json()['detail'] == error_msg.login_fail

    def test_get_user_me(self, test_client, test_user):
        token = self.get_token(test_client, test_user)
        response = test_client.get(f"/{self.collection}/me",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 200
        assert self.compare_response_and_test_users(response, test_user)

    def test_get_user_me_without_auth(self, test_client):
        response = test_client.get(f"/{self.collection}/me")
        assert response.status_code == 401
        assert response.json()['detail'] == error_msg.not_auth_user

    def test_get_user_me_wrong_token(self, test_client):
        token = 'wrong token'
        response = test_client.get(f"/{self.collection}/me",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 401
        assert response.json()['detail'] == error_msg.invalid_credentials

    def test_admin_get_existing_user(self, test_client, test_admin, test_user):
        token = self.get_token(test_client, test_admin)
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
        assert response.json()['detail'] == error_msg.invalid_credentials

    def test_fail_get_not_existing_user(self, test_client, test_admin):
        token = self.get_token(test_client, test_admin)
        id = '645b4d9e5f81141374088b6c'
        response = test_client.get(f"/{self.collection}/{id}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 400
        assert response.json()['detail'] == error_msg.instance_not_exists

    def test_fail_get_not_valid_id(self, test_client, test_admin):
        token = self.get_token(test_client, test_admin)
        id = 'invalid id'
        response = test_client.get(f"/{self.collection}/{id}",
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 400
        assert response.json()['detail'] == error_msg.invalid_id

    def test_delete_me(self, test_client, test_user):
        token = self.get_token(test_client, test_user)
        response = test_client.delete(f"/{self.collection}/me",
                                      headers={'Authorization':
                                               f'Bearer {token}'})
        assert response.status_code == 204
        try:
            authenticated_user(token)
            assert False
        except AttributeError:
            assert True

    def test_admin_delete_user(self, test_client, test_user, test_admin):
        token_user = self.get_token(test_client, test_user)
        token_admin = self.get_token(test_client, test_admin)

        user = authenticated_user(token_user)

        response = test_client.delete(f"/{self.collection}/{user.id}",
                                      headers={'Authorization':
                                               f'Bearer {token_admin}'})
        assert response.status_code == 204

        assert len(test_client.get(f"/{self.collection}",
                                   headers={'Authorization':
                                            f'Bearer {token_admin}'}).json()) == 1

    def test_user_delete_user(self, test_client, test_user):
        token_user = self.get_token(test_client, test_user)

        user = authenticated_user(token_user)

        response = test_client.delete(f"/{self.collection}/{user.id}",
                                      headers={'Authorization':
                                               f'Bearer {token_user}'})
        assert response.status_code == 401
        assert response.json()['detail'] == error_msg.invalid_credentials

    def test_update_me(self, test_client, test_user, test_user_updated):
        token = self.get_token(test_client, test_user)

        response = test_client.put(f"/{self.collection}/me",
                                   data=test_user_updated,
                                   headers={'Authorization':
                                            f'Bearer {token}'})
        assert response.status_code == 200
        user = authenticated_user(token)
        print(user.name)
        assert user.name == 'Test user updated'
