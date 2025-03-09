from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
# from pydantic import BaseModel

from model.settings.db_connection_handler import db_connection_handler
from views.people_finder_view import PeopleFinderView
from views.people_creator_view import PeopleCreatorView
from views.people_updater_view import PeopleUpdaterView
from views.people_deleter_view import PeopleDeleterView


people_routes = APIRouter()


# class PersonaSchema(BaseModel):
#     name: str


@people_routes.get("/people")
async def get_people(request: Request):
    people_finder_view = PeopleFinderView()

    await db_connection_handler.connect_to_db()
    http_response = await people_finder_view.handle_find_people()
    await db_connection_handler.disconnect_to_db()

    return JSONResponse(
        content=http_response["body"],
        status_code=http_response["status_code"]
    )


@people_routes.post("/people")
async def create_persona(request: Request):
    try:
        body = await request.json()
        people_creator_view = PeopleCreatorView()

        await db_connection_handler.connect_to_db()
        http_response = await people_creator_view.handle_create_persona(body)
        await db_connection_handler.disconnect_to_db()

        return JSONResponse (
            content=http_response["body"],
            status_code = http_response["status_code"]
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@people_routes.put("/people/{id}")
async def update_persona(id: int, request: Request):
    try:
        body = await request.json()
        people_updater_view = PeopleUpdaterView()

        await db_connection_handler.connect_to_db()
        http_response = await people_updater_view.handle_update_persona(id, body)
        await db_connection_handler.disconnect_to_db()

        return JSONResponse(
            content=http_response["body"],
            status_code=http_response["status_code"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@people_routes.delete("/people/{id}")
async def delete_persona(id: int):
    try:
        people_deleter_view = PeopleDeleterView()

        await db_connection_handler.connect_to_db()
        http_response = await people_deleter_view.handle_delete_persona(id)
        await db_connection_handler.disconnect_to_db()

        return JSONResponse(
            content=http_response["body"],
            status_code=http_response["status_code"]
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



