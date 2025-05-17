import graphene


def main():
    print("Hello from monograph!")


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()


class Query(graphene.ObjectType):
    get_user = graphene.Field(User)

    @staticmethod
    def resolve_get_user(root, info):
        return User(id="1", username="test")


schema = graphene.Schema(query=Query)
results = schema.execute("""
    query {
        getUser {
            id
        }
    }
""")

print(results.data)
