import requests
import pytest


@pytest.mark.placeholder
class TestPlaceholderAPI:

    def test_get_posts_list(self, base_url, status_code):
        response = requests.get(base_url + '/posts')
        assert response.status_code == int(status_code)
        assert len(response.json()) == 100

    def test_get_comments_list(self, base_url, status_code):
        response = requests.get(base_url + '/comments')
        assert response.status_code == int(status_code)
        assert len(response.json()) == 500

    def test_get_random_post(self, base_url, status_code, get_random_id):
        response = requests.get(base_url + f"/posts/{get_random_id}")
        assert response.status_code == int(status_code)
        assert response.json()['id'] == get_random_id

    @pytest.mark.parametrize("input_testId, exp_testId", [(1, '1'), (3, '3')])
    @pytest.mark.parametrize("input_body, exp_body", [('test', 'test')])
    @pytest.mark.parametrize("input_list, exp_list", [(['a', 'b'], ['a', 'b']), ([1, 2, 3], ['1', '2', '3'])])
    def test_api_post_request(self, base_url, input_testId, exp_testId,
                              input_body, exp_body, input_list, exp_list):
        response = requests.post(
            base_url + "/posts",
            data={'testId': input_testId,
                  'body': input_body,
                  'some_list': input_list}
        )
        assert response.status_code == 201
        assert response.json()["testId"] == exp_testId
        assert response.json()["body"] == exp_body
        assert response.json()["some_list"] == exp_list

    @pytest.mark.parametrize("test_id", [1, 3, 70])
    @pytest.mark.parametrize("input_testId, exp_testId", [(1, '1'), (3, '3')])
    @pytest.mark.parametrize("input_body, exp_body", [('test', 'test')])
    @pytest.mark.parametrize("input_list, exp_list", [(['a', 'b'], ['a', 'b']), ([1, 2, 3], ['1', '2', '3'])])
    def test_api_put_request(self, base_url, status_code, input_testId, test_id,
                             exp_testId, input_body, exp_body, input_list, exp_list):
        response = requests.put(
            base_url + f"/posts/{test_id}",
            data={'testId': input_testId,
                  'body': input_body,
                  'some_list': input_list}
        )
        assert response.status_code == int(status_code)
        assert response.json()["id"] == test_id
        assert response.json()["testId"] == exp_testId
        assert response.json()["body"] == exp_body
        assert response.json()["some_list"] == exp_list
