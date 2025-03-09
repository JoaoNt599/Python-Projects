from controllers.people_creator import PeopleCreator


class PeopleCreatorView:
    
    def __init__(self):
        self.__people_creator = PeopleCreator()

    
    async def handle_create_persona(self, request: dict):
        create_persona = await self.__people_creator.create_persona(request)

        return {
            "status_code": 201,
            "body": created_persona
        }