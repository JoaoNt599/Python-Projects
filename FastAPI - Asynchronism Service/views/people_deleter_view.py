from controllers.people_deleter import PeopleDeleter


class PeopleDeleterView:

    def __init__(self):
        self.__people_deleter = PeopleDeleter()

    async def handle_delete_persona(self, id: int):
        deleted_persona = await self.__people_deleter.delete_persona(id)

        return {
            "status_code": 200,
            "body": {"message": "Persona deleted successfully"}
        }
