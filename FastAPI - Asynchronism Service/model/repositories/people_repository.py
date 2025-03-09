from model.settings.db_connection_handler import db_connection_handler
from model.entities.people import People
from sqlalchemy import insert


class PeopleRepository:

    def __init__(self):
        self.__conn = db_connection_handler.get_db_conn()
    
    async def get_all_people(self) -> list:
        query = People.select()
        result = await self.__conn.fetch_all(query)
        return result


    async def insert_persona(self, name: str):
        query = "INSERT INTO people (name) VALUES (:name)"
        values = {"name": name}

        db = db_connection_handler.get_db_conn()
        await db.execute(query=query, values=values)

        last_id = await db.fetch_val("SELECT last_insert_rowid()")

        return {"id": None, "name": name}


    async def update_persona(self, id, name):
        query = "UPDATE people SET name = :name WHERE id = :id"
        values = {"id": id, "name": name}

        db = db_connection_handler.get_db_conn()
        await db.execute(query=query, values=values)

        return People(id=id, name=name)
    

    async def delete_persona(self, id):
        query = "DELETE FROM people WHERE id = :id"
        values = {"id": id}

        db = db_connection_handler.get_db_conn()
        await db.execute(query=query, values=values)

    
    async def get_persona_by_id(self, id):
        query = "SELECT * FROM people WHERE id = :id"
        values = {"id": id}

        db = db_connection_handler.get_db_conn()
        result = await db.fetch_one(query=query, values=values)

        if result:
            return People(id=result["id"], name=result["name"])
        return None



    

