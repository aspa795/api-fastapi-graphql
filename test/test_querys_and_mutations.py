def test_create_post(client):
    query = """
    mutation {
      createPost(postDetails: {
        userId: 1,
        title: "This title!!!",
        body: "Body test text!!!"
      })
      {
        code
        message
        body{
          id,
          title,
          body,
          userId
        }
      }
    }
    """

    result = client.execute(query)
    assert result['data']['createPost']['id'] == 1
    assert result['data']['createPost']['title'] == "This title!!!"


def test_get_list_post(client):
    query = """
    query {
       listPosts{
        id,
        title,
        body,
        userId
      }
    }
    """

    result = client.execute(query)
    assert type(result['data']['listPosts']) == list


def test_get_single_post(client, post):
    query = """
    query {
      getSinglePost(postId: %s) {
        id,
        title,
        body,
        userId
      }
    }
    """ % post.id
    result = client.execute(query)
    assert result['data']['getSinglePost'] is not None
    assert result['data']['getSinglePost']['title'] == post.title
