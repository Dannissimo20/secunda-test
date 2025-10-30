from pydantic import UUID4, Field

from src.app.schemas.activity_schema import ActivityOut
from src.app.schemas.base_schema import BaseSchema
from src.app.schemas.building_schema import Building


class OrganizationOut(BaseSchema):
    id: UUID4 = Field(..., description="Уникальный идентификатор организации")
    name: str = Field(..., max_length=255, description="Название организации", examples=["ООО \"Рога и Копыта\""])
    phone: list[str] = Field(..., description="Массив с номерами телефонов", examples=["[\"2-222-222\", \"3-333-333\", \"8-923-666-13-13\"]"])
    building: Building = Field(..., description="Здание в котором находится организация")
    activities: list[ActivityOut] = Field(..., description="Список родов деятельности организации")
