from flask_graphql import GraphQLView
from app import app, db
from app.schema import schema
from app.models import Notes

db.create_all()
app.add_url_rule("/", view_func=GraphQLView.as_view("graphql",
                 schema=schema, graphiql=True))


if __name__ == "__main__":
    app.run(debug=True)
