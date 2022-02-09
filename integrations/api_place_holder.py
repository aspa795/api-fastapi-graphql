from urllib.request import Request
import requests

url_base = 'https://jsonplaceholder.typicode.com'
headers = {
    'Content-type': 'application/json; charset=UTF-8',
}


def get_posts():

    try:
        response = requests.get(url='{}/posts'.format(url_base))

        if response.status_code == 200:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': []}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}


def get_post(post_id: int):

    try:
        response = requests.get(url='{}/posts/{}'.format(url_base, post_id))

        if response.status_code == 200:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': {}}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}


def get_all_comments_of_a_post(post_id: int):

    try:
        response = requests.get(
            url='{}/posts/{}/comments'.format(url_base, post_id))

        if response.status_code == 200:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': []}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}


def get_comments_of_a_post(post_id: int):

    try:
        response = requests.get(
            url='{}/comments?postId={}'.format(url_base, post_id))

        if response.status_code == 200:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': []}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}


def create_post(body_request):

    try:
        response = requests.post(
            '{}/posts'.format(url_base), data=body_request, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': {}}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}


def update_post(post_id: int, body_request):

    try:
        response = requests.put(
            '{}/posts/{}'.format(url_base, post_id), data=body_request, headers=headers)

        if response.status_code == 200 or response.status_code == 204:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': {}}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}


def patch_post(post_id: int, body_request):

    try:
        response = requests.patch(
            '{}/posts/{}'.format(url_base, post_id), data=body_request, headers=headers)
        if response.status_code == 200 or response.status_code == 204:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': {}}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}


def delete_post(post_id: int):

    try:
        response = requests.delete(
            '{}/posts/{}'.format(url_base, post_id), headers=headers)

        if response.status_code == 200:
            return {'code': response.status_code, 'data': response.json()}
        return {'code': response.status_code, 'data': {}}
    except requests.exceptions.RequestException as error:
        return {'code': 500, 'error': error}
