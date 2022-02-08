import graphene

from serializers.post_serializer import (
    PostGrapheneInputModel, PostGrapheneModel)


from models.post import Post


class Query(graphene.ObjectType):
    list_posts = graphene.List(PostGrapheneModel)
    get_single_post = graphene.Field(
        PostGrapheneModel, postId=graphene.NonNull(graphene.Int))

    @staticmethod
    def resolve_list_posts(parent, info):
        return Post.all()

    @staticmethod
    def resolve_get_single_post(parent, info, postId):
        return Post.find_or_fail(postId)


class CreatePost(graphene.Mutation):
    class Arguments:
        post_details = PostGrapheneInputModel()

    Output = PostGrapheneModel

    @staticmethod
    def mutate(parent, info, post_details):
        post = Post()
        post.userId = post_details.userId
        post.title = post_details.title
        post.body = post_details.body

        post.save()

        return post


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
