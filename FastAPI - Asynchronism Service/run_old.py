import asyncio

from model.settings.db_initializer import create_tables, seed_people
from model.settings.db_connection_handler import db_connection_handler
from controllers.people_finder import PeopleFinder


async def run_people():
    await db_connection_handler.connect_to_db()

    controller = PeopleFinder()
    response = await controller.find_people()

    print(response)

    await db_connection_handler.disconnect_to_db()


if __name__ == "__main__":
    # create_tables()  
    # asyncio.run(seed_people())
    asyncio.run(run_people())  

