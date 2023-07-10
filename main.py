

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema


from services.config import Config
from services.db import DB


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
