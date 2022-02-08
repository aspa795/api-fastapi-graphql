from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class CommentsModel(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class CommentGrapheneModel(PydanticObjectType):
    class Meta:
        model = CommentsModel


class CommentGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = CommentsModel
        exclude_fields = ('id', )
