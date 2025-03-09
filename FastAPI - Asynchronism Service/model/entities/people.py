from model.settings.db_metadata import metadata
from sqlalchemy import MetaData, Table, Column, Integer, String 


People = Table(
    "people", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String) 
)