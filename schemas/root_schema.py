import graphene

from schemas import (post_schema, comment_schema)

class Query(post_schema.Query, comment_schema.Query, graphene.ObjectType):
    pass


class Mutation(post_schema.Mutation, comment_schema.Mutation, graphene.ObjectType):
    pass
