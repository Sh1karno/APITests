import requests
import pytest
import random


@pytest.mark.placeholder
class TestPlaceholderAPI:

    def test_get_posts_list(self, placeholder, status_code):
        response = placeholder.get_posts_list()
        assert response.status_code == int(status_code)
        assert len(response.json()) == 100

    def test_get_comments_list(self, placeholder, status_code):
        response = placeholder.get_comments_list()
        assert response.status_code == int(status_code)
        assert len(response.json()) == 500

    def test_get_random_post(self, placeholder, status_code):
        random_id = random.randint(1, 100)
        response = placeholder.get_post(random_id)
        assert response.status_code == int(status_code)
        assert response.json()['id'] == random_id

    @pytest.mark.parametrize("input_testId, exp_testId", [(1, '1'), (3, '3')])
    @pytest.mark.parametrize("input_body, exp_body", [('test', 'test')])
    @pytest.mark.parametrize("input_list, exp_list", [(['a', 'b'], ['a', 'b']), ([1, 2, 3], ['1', '2', '3'])])
    def test_api_post_request(self, placeholder, input_testId, exp_testId,
                              input_body, exp_body, input_list, exp_list):
        response = placeholder.post_data(input_testId, input_body, input_list)
        json_response = response.json()
        assert response.status_code == 201
        assert json_response["testId"] == exp_testId
        assert json_response["body"] == exp_body
        assert json_response["some_list"] == exp_list

    @pytest.mark.parametrize("test_id", [1, 3, 70])
    @pytest.mark.parametrize("input_testId, exp_testId", [(1, '1'), (3, '3')])
    @pytest.mark.parametrize("input_body, exp_body", [('test', 'test')])
    @pytest.mark.parametrize("input_list, exp_list", [(['a', 'b'], ['a', 'b']), ([1, 2, 3], ['1', '2', '3'])])
    def test_api_put_request(self, placeholder, status_code, input_testId, test_id,
                             exp_testId, input_body, exp_body, input_list, exp_list):
        response = placeholder.put_data(test_id, input_testId, input_body, input_list)
        json_response = response.json()
        assert response.status_code == int(status_code)
        assert json_response["id"] == test_id
        assert json_response["testId"] == exp_testId
        assert json_response["body"] == exp_body
        assert json_response["some_list"] == exp_list
