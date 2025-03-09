from model.repositories.people_repository import PeopleRepository


class PeopleFinder:

    def __init__(self):
        self.__people_repo = PeopleRepository()

    async def find_people(self) -> dict:
        people = await self.__people_repo.get_all_people()
        if people == []: raise Exception("People not found")

        formatted_people = []

        for persona in people:
            if persona.name == "Bob": continue
            formatted_people.append(
                {
                    "id": persona.id,
                    "name": persona.name
                }
            )

        return {
            "type": "Persona",
            "count": len(formatted_people),
            "attributes": formatted_people
        } 
