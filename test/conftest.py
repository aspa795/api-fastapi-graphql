import graphene
import pytest
from graphene.test import Client
from orator import DatabaseManager, Model, Schema
from orator.migrations import DatabaseMigrationRepository, Migrator

from models.comment import Comment
from models.post import Post
from schemas.root_schema import Query, Mutation


@pytest.fixture(autouse=True)
def setup_database():
    DATABASES = {
        "sqlite": {
            "driver": "sqlite",
            "database": "test.db"
        }
    }

    db = DatabaseManager(DATABASES)
    Schema(db)

    Model.set_connection_resolver(db)

    repository = DatabaseMigrationRepository(db, "migrations")
    migrator = Migrator(repository, db)

    if not repository.repository_exists():
        repository.create_repository()

    migrator.reset("migrations")
    migrator.run("migrations")


@pytest.fixture(scope="module")
def client():
    client = Client(schema=graphene.Schema(query=Query, mutation=Mutation))
    return client


@pytest.fixture(scope="function")
def post():
    post = Post()
    post.title = "Test Title"
    post.body = "this is the post body and can be as long as possible"
    post.userId = 1

    post.save()
    return post


@pytest.fixture(scope="function")
def comment():
    comment = Comment()
    comment.postId = 2
    comment.name = 'Name test'
    comment.email = 'email@email.com'
    comment.body = 'Body test'

    comment.save()

    return comment