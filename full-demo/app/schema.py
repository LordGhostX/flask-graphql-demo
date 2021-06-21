from datetime import datetime
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
    note = graphene.Field(lambda: Note)

    def mutate(self, info, title, body):
        note = Notes(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        return createNote(note=note)


class updateNote(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        title = graphene.String()
        body = graphene.String()
    note = graphene.Field(lambda: Note)

    def mutate(self, info, id, title, body):
        update_data = {
            "title": title,
            "body": body,
            "last_updated": datetime.utcnow()
        }
        Notes.query.filter_by(id=id).update(update_data)
        db.session.commit()
        return updateNote(note=Notes.query.get(id))


class deleteNote(graphene.Mutation):
    class Arguments:
        id = graphene.String()
    ok = graphene.Boolean()

    def mutate(self, info, id):
        db.session.delete(Notes.query.get(id))
        db.session.commit()
        return deleteNote(ok=True)


class Mutation(graphene.ObjectType):
    createNote = createNote.Field()
    updateNote = updateNote.Field()
    deleteNote = deleteNote.Field()


class Query(graphene.ObjectType):
    all_notes = graphene.List(Note)
    get_note = graphene.Field(Note, id=graphene.String(required=True))

    def resolve_all_notes(self, info):
        return Notes.query.all()

    def resolve_get_note(self, info, id):
        return Notes.query.get(id)


schema = graphene.Schema(query=Query, mutation=Mutation)
