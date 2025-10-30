from pydantic import UUID4, Field
from src.app.schemas.base_schema import BaseSchema


class Building(BaseSchema):
    id: UUID4 = Field(..., description="Уникальный идентификатор здания")
    address: str = Field(max_length=1023, description="Полный адрес здания", examples=["г. Москва, ул. Ленина 1, офис 3"])
    latitude: float = Field(..., ge=-90, le=90, description="Географичекая широта", examples=[50.88888888])
    longitude: float = Field(..., ge=-180, le=180, description="Географичекая долгота", examples=[50.88888888])
