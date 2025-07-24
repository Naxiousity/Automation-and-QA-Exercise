import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://automationexercise.com/api"

@pytest.fixture
def session():
    return requests.Session()