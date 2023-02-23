import os
from time import sleep
from news.utils import generate_data


def test_generate_data_mock():
    if os.path.exists("mocks/news.json"):
        os.remove("mocks/news.json")
    generate_data()
    sleep(2)
    assert os.path.exists("mocks/news.json")
