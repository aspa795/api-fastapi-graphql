from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class PostModel(BaseModel):
    id: int
    userId: int
    title: str
    body: str


class PostGrapheneModel(PydanticObjectType):
    class Meta:
        model = PostModel


class PostGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = PostModel
        exclude_fields = ('id', )
