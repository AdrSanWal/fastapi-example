import json
from pytest import mark


@mark.users
class TestUsers():
    collection = 'users'

    def test_get_users(self, test_client):
        response = test_client.get(f"/{self.collection}")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_post_user(self, test_client, test_user, test_image):
        response = test_client.post(f"/{self.collection}",
                                    files=test_image,
                                    data=test_user)
        assert response.status_code == 201

    def test_post_existing_user(self, test_client, test_user, test_image):
        test_client.post(f"/{self.collection}",
                         files=test_image,
                         data=test_user)
        response = test_client.post(f"/{self.collection}",
                                    files=test_image,
                                    data=test_user)
        assert response.status_code == 409

    def test_get_existing_user(self, test_client, test_user, test_image):
        response = test_client.post(f"/{self.collection}",
                                    files=test_image,
                                    data=test_user)
        id = response.json()['id']
        response = test_client.get(f"/{self.collection}/{id}")
        assert response.status_code == 200

        response_user = dict(response.json())
        del response_user['id']
        del response_user['image']
        assert response_user == test_user

    def test_fail_get_not_existing_user(self, test_client):
        id = '645b4d9e5f81141374088b6c'
        response = test_client.get(f"/{self.collection}/{id}")
        assert response.status_code == 400
        assert response.json()['detail'] == 'Element not exists'

    def test_fail_get_not_valid_id(self, test_client):
        id = 'invalid id'
        response = test_client.get(f"/{self.collection}/{id}")
        assert response.status_code == 400

        expected_msg = 'invalid id is not a valid ObjectId, it must be a ' \
            + '12-byte input ora 24-character hex string'
        assert response.json()['detail'] == expected_msg

    def test_delete_user(self, test_client, test_user, test_image):
        response = test_client.post(f"/{self.collection}",
                                    files=test_image,
                                    data=test_user)
        id = response.json()['id']
        assert len(test_client.get(f"/{self.collection}").json()) == 1

        response = test_client.delete(f"/{self.collection}/{id}")
        assert response.status_code == 204

        assert len(test_client.get(f"/{self.collection}").json()) == 0

    def test_update_user(self, test_client, test_user, test_user_updated, test_image):
        response = test_client.post(f"/{self.collection}",
                                    files=test_image,
                                    data=test_user)
        id = response.json()['id']
        response = test_client.put(f"/{self.collection}/{id}",
                                   content=json.dumps(test_user_updated))
        assert response.status_code == 200

        updated_db_user = test_client.get(f"/{self.collection}/{id}").json()
        test_user_updated['id'] = id
        assert updated_db_user == test_user_updated
