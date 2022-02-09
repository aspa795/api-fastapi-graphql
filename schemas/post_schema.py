import graphene
from pydantic.dataclasses import Optional

from serializers.post_serializer import (
    PostGrapheneInputModel, PostGrapheneUpdateInputModel, PostGrapheneModel, PostGraphenePatchInputModel)
from serializers.comment_serializer import (CommentGrapheneModel)

from models.post import Post
from models.comment import Comment


class Query(graphene.ObjectType):
    list_posts = graphene.List(PostGrapheneModel)
    get_single_post = graphene.Field(
        PostGrapheneModel, post_id=graphene.NonNull(graphene.Int))
    get_comments_by_post = graphene.List(CommentGrapheneModel, post_id=graphene.NonNull(graphene.Int))

    @staticmethod
    def resolve_list_posts(parent, info):
        return Post.all()

    @staticmethod
    def resolve_get_single_post(parent, info, post_id):
        return Post.find_or_fail(post_id)

    @staticmethod
    def resolve_get_comments_by_post(parent, info, post_id):
        return Comment.all().where('postId', post_id)


class CreatePost(graphene.Mutation):
    class Arguments:
        post_details = PostGrapheneInputModel()

    code = graphene.Int()
    message = graphene.String()
    body = graphene.Field(PostGrapheneModel)

    @staticmethod
    def mutate(parent, info, post_details):
        try:
            post = Post()

            post.userId = post_details.userId
            post.title = post_details.title
            post.body = post_details.body
            post.save()

            return CreatePost(code=201, message='Post Create Success', body=post)
        except Exception as e:
            return CreatePost(code=400, message=str(e))


class UpdatePost(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int(required=True)
        post_details = PostGrapheneUpdateInputModel()

    code = graphene.Int()
    message = graphene.String()
    body = graphene.Field(PostGrapheneModel)

    @staticmethod
    def mutate(parent, info, post_id, post_details):
        try:
            post = Post.find_or_fail(post_id)
            post.id = post_details.id
            post.userId = post_details.userId
            post.title = post_details.title
            post.body = post_details.body
            post.save()

            return UpdatePost(code=200, message='Post Update Success', body=post)
        except Exception as e:
            return UpdatePost(code=400, message=str(e))


class PatchPost(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int(required=True)
        post_details = PostGraphenePatchInputModel()

    code = graphene.Int()
    message = graphene.String()
    body = graphene.Field(PostGrapheneModel)

    @staticmethod
    def mutate(parent, info, post_id, post_details):
        try:
            post = Post.find_or_fail(post_id)
            [post.set_attribute(key=key, value=post_details[key]) for key in post_details]
            post.save()

            return PatchPost(code=200, message='Post Update Fields Success', body=post)

        except Exception as e:
            return PatchPost(code=400, message=str(e))


class DeletePost(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int(required=True)

    code = graphene.Int()
    message = graphene.String()

    @staticmethod
    def mutate(parent, info, post_id):
        try:
            post = Post.find_or_fail(post_id)
            post.delete()

            return UpdatePost(code=200, message='Post Delete Success')
        except Exception as e:
            return UpdatePost(code=400, message=str(e))


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    patch_post = PatchPost.Field()
    delete_post = DeletePost.Field()
