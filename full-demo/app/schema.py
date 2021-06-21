import graphene
from app import db
from app.models import Notes


class Note(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    body = graphene.String()
    last_updated = graphene.DateTime()
    date_created = graphene.DateTime()


class createNote(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        body = graphene.String()
    ok = graphene.Boolean()
    note = graphene.Field(lambda: Note)

    def mutate(self, info, title, body):
        note = Notes(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        return createNote(note=note, ok=True)


class Mutation(graphene.ObjectType):
    createNote = createNote.Field()


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(required=True))

    def resolve_hello(self, info, name):
        return f"Hello {name}!"


schema = graphene.Schema(query=Query, mutation=Mutation)
