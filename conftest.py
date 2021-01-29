import pytest
import requests
import random


from datetime import datetime
from operator import itemgetter


@pytest.fixture(scope="session", autouse=True)
def set_time_testrun():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print('\nTEST-RUN RUNTIME:', end_time - start_time)


@pytest.fixture(scope="function", autouse=True)
def set_time_test():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(' | test-case runtime:', end_time - start_time)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
        )

    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        help="This status code"
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='session')
def status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def get_dict_breeds(base_url):
    response = requests.get(base_url + '/api/breeds/list/all')
    return response.json()['message']


# This fixture give random breed from all breeds
@pytest.fixture
def get_random_breed(get_dict_breeds):
    list_breeds = [breed for breed in get_dict_breeds.keys()]
    random_breed = random.choice(list_breeds)
    return random_breed


@pytest.fixture
def get_random_breweries(base_url):
    response = requests.get(base_url + '/breweries')
    return random.choice(response.json())


# Using this fixture in test_breweries_by_name_and_sort to get expected result
@pytest.fixture
def get_sorted_response_by_id(base_url):
    response = requests.get(base_url + '/breweries?by_city=Alameda').json()
    response.sort(key=itemgetter('id'))
    return response


@pytest.fixture
def get_random_id():
    random_id = random.randint(1, 100)
    return random_id
