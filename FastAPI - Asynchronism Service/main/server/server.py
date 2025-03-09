from fastapi import FastAPI
from main.routes.people_routes import people_routes


app = FastAPI()
app.include_router(people_routes)
