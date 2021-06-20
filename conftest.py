import pytest
import random

from wrappers.base_request import BaseRequest
from wrappers.breweries import Breweries
from wrappers.placeholder import Placeholder
from wrappers.dogs import Dogs
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


@pytest.fixture(scope='session')
def base_method(base_url):
    method = BaseRequest(base_url)
    return method


@pytest.fixture(scope='session')
def dogs():
    return Dogs()


@pytest.fixture(scope='session')
def breweries():
    return Breweries()


@pytest.fixture(scope='session')
def placeholder():
    return Placeholder()


@pytest.fixture(scope='function')
def dict_breeds(dogs):
    response = dogs.get_all_breeds_list()
    return response.json()['message']


# This fixture give random breed from all breeds
@pytest.fixture(scope='function')
def random_breed(dict_breeds):
    list_breeds = [breed for breed in dict_breeds.keys()]
    return random.choice(list_breeds)


@pytest.fixture(scope='function')
def random_breweries(breweries):
    response = breweries.get_breweries_list()
    return random.choice(response.json())


# Using this fixture in test_breweries_by_name_and_sort to get expected result
@pytest.fixture(scope='function')
def sorted_response_by_id(breweries):
    response = breweries.get_breweries_list({'by_name': 'Alameda'}).json()
    response.sort(key=itemgetter('id'))
    return response
