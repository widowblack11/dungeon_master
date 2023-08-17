import requests


def post_v1_account_ligin():
    """
        Authenticate via credentials
        :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login"

    payload = ({
        "login": "test_vvvv_123",
        "password": "test_vvvv_123",
        "rememberMe": False
    })

    headers = {
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    return response
