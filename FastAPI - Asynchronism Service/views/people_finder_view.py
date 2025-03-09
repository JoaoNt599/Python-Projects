from controllers.people_finder import PeopleFinder


class PeopleFinderView:

    def __init__(self):
        self.__controller = PeopleFinder()

    async def handle_find_people(self, http_request = None) -> dict:
        response = await self.__controller.find_people()
        http_response = {
            "body": response,
            "status_code": 200
        }
        return http_response

