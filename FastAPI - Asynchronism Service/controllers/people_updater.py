from model.repositories.people_repository import PeopleRepository


class PeopleUpdater:

    def __init__(self):
        self.__people_repo = PeopleRepository()

    async def update_persona(self, id: int, data: dict):
        name = data.get("name")

        if not name:
            raise Exception("Name is required")

        updated_persona = await self.__people_repo.update_persona(id, name)

        return {
            "id": updated_persona.id,
            "name": updated_persona.name
        }
