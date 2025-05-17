import strawberry
from strawberry.schema.config import StrawberryConfig


from app.handlers.graphql.mutation import UserMutations
from app.handlers.graphql.query import UserQuery


@strawberry.type
class Mutation:
    users: UserMutations = strawberry.field(resolver=lambda: UserMutations())


@strawberry.type
class Query:
    users: UserQuery = strawberry.field(resolver=lambda: UserQuery())


schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))
