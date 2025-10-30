from sqlalchemy import select
from src.app.database.database import DBWriter
from src.app.models import Building
from src.app.schemas.building_schema import Building as BuildingSchema


class BuildingRepo:
    def __init__(self, db: DBWriter):
        self.db = db


    def get_all(self) -> list[BuildingSchema]:
        query = select(Building)

        with self.db.session() as session:
            result = session.execute(query).scalars().all()
            return [BuildingSchema.model_validate(item) for item in result]
