import graphene

from serializers.comment_serializer import (
    CommentGrapheneInputModel, CommentGrapheneModel)

from models.comment import Comment


class Query(graphene.ObjectType):
    list_comments = graphene.List(CommentGrapheneModel)

    @staticmethod
    def resolve_list_comments(parent, info):
        return Comment.all()


class CreateComment(graphene.Mutation):
    class Arguments:
        comment_details = CommentGrapheneInputModel()

    Output = CommentGrapheneModel

    @staticmethod
    def mutate(parent, info, comment_details):
        comment = Comment()

        comment.postId = comment_details.postId
        comment.name = comment_details.name
        comment.email = comment_details.email
        comment.body = comment_details.body

        comment.save()

        return comment

class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()