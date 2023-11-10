from random import randint

import requests


def make_get_call(endpoint: str, params: dict):
    print(requests.get(endpoint, params=params).text)


def sum_call(n: int = 1):
    endpoint = "http://localhost:8000/sum"
    for _  in range(n):
        params = {
            "val1": randint(0, 10000),
            "val2": randint(0, 10000)
        }
        make_get_call(endpoint, params)


if __name__ == "__main__":
    sum_call(10)
