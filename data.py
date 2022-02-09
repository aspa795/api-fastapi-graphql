from integrations.api_place_holder import get_posts
from models.post import Post


def fill_data():
    try:
        response = get_posts()
        print('Inserting posts in the database...')
        for post in response['data']:
            new_post = Post()
            [new_post.set_attribute(key=key, value=post[key]) for key in post if key != 'id']
            new_post.save()
        print('Process success!!')

    except Exception as e:
        print('error:' + str(e))


fill_data()
