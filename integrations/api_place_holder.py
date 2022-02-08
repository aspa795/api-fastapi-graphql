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
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}


def get_post(postId: int):

    try:
        response = requests.get(url='{}/posts/{}'.format(url_base, postId))

        if response.status_code == 200:
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}


def get_all_comments_of_a_post(postId: int):

    try:
        response = requests.get(
            url='{}/posts/{}/comments'.format(url_base, postId))

        if response.status_code == 200:
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}


def get_comments_of_a_post(postId: int):

    try:
        response = requests.get(
            url='{}/comments?postId={}'.format(url_base, postId))

        if response.status_code == 200:
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}


def create_post(body_request):

    try:
        response = requests.post(
            '{}/posts'.format(url_base), data=body_request, headers=headers)

        if response.status_code == 201:
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}


def update_post(postId: int, body_request):

    try:
        response = requests.put(
            '{}/posts/{}'.format(url_base, postId), data=body_request, headers=headers)

        if response.status_code == 200:
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}


def patch_post(postId: int, body_request):
    
    try:
        response = requests.patch(
            '{}/posts/{}'.format(url_base, postId), data=body_request, headers=headers)

        if response.status_code == 200:
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}


def delete_post(postId: int):

    try:
        response = requests.delete(
            '{}/posts/{}'.format(url_base, postId), headers=headers)

        if response.status_code == 200:
            return response.text
        return {}
    except requests.exceptions.RequestException as error:
        return {'error': error}
