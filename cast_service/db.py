from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://postgres:postgres@localhost/cast_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

casts = Table(
    'cast',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
)

database = Database(DATABASE_URL)
