import requests


def delete_v1_account_delete():
    """"
    Logout from every device
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login/all"

    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="DELETE",
        url=url,
        headers=headers
    )

    return response
