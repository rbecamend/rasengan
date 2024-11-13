from peewee import IntegerField, PrimaryKeyField, BooleanField

from config.db import BaseModel, pg_db


class Nup (BaseModel):
    nup = IntegerField(unique=True)
    id = PrimaryKeyField()
    cadastrado = BooleanField(default=False)

def create_table():
    with pg_db:
        pg_db.create_table(Nup)