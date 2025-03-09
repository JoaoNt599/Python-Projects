from model.repositories.people_repository import PeopleRepository


class PeopleDeleter:

    def __init__(self):
        self.__people_repo = PeopleRepository()

    async def delete_persona(self, id: int):
        person = await self.__people_repo.get_persona_by_id(id)
        if not person:
            raise Exception("Person not found")

        await self.__people_repo.delete_persona(id)
        return True
