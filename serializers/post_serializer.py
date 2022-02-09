from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel
from pydantic.dataclasses import Optional


class PostModel(BaseModel):
    id: int
    userId: int
    title: str
    body: str


class PostModelPatch(BaseModel):
    id: Optional[int] = None
    userId: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None


class PostGrapheneModel(PydanticObjectType):
    class Meta:
        model = PostModel


class PostGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = PostModel
        exclude_fields = ('id', )


class PostGrapheneUpdateInputModel(PydanticInputObjectType):
    class Meta:
        model = PostModel


class PostGraphenePatchInputModel(PydanticInputObjectType):
    class Meta:
        model = PostModelPatch

