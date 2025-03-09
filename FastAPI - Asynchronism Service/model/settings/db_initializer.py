from sqlalchemy import create_engine
from model.settings.db_metadata import metadata
from sqlalchemy import insert
from model.entities.people import People
from model.settings.db_connection_handler import db_connection_handler


def create_tables():
    engine = create_engine("sqlite:///db.sqlite")
    metadata.create_all(engine)
    print("Created")

async def seed_people():
    query = insert(People).values(
        [
            {"name": "Alice"},
            {"name": "Bob"},
            {"name": "Charlie"}
        ]
    )

    await db_connection_handler.connect_to_db()
    await db_connection_handler.get_db_conn().execute(query)
    await db_connection_handler.connect_to_db()
    print("Insert People")
