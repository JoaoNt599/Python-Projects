from controllers.people_updater import PeopleUpdater


class PeopleUpdaterView:

    def __init__(self):
        self.__people_updater = PeopleUpdater()

    async def handle_update_persona(self, id: int, request: dict):
        updated_persona = await self.__people_updater.update_persona(id, request)

        return {
            "status_code": 200,
            "body": updated_persona
        }
