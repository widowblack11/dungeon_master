import requests


def put_v1_account_email():
    """
    Change registered user email
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/email"

    payload = ({
        "login": "test_vvvv_123",
        "password": "test_vvvv_123",
        "email": "dldldldldl@mail.ru"
    })

    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )

    return response
