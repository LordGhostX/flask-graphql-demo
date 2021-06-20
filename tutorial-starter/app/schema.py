import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(required=True))

    def resolve_hello(self, info, name):
        return f"Hello {name}!"


schema = graphene.Schema(query=Query)
