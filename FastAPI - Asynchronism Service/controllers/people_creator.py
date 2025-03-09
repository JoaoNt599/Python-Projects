from model.repositories.people_repository import PeopleRepository


class PeopleCreator:

    def __init__(self):
        self.__people_repo = PeopleRepository()

    async def create_persona(self, data: dict):
        name = data.get("name")

        if not name:
            raise Exception("Name is required")

        new_person = await self.__people_repo.insert_persona(name)

        return {
            "id": new_person.id,
            "name": new_person.name
        }
