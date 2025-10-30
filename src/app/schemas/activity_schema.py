from pydantic import UUID4, Field
from src.app.schemas.base_schema import BaseSchema


class ActivityOut(BaseSchema):
    id: UUID4 = Field(..., description="Уникальный идентификатор деятельности")
    name: str = Field(..., max_length=255, description="Название рода деятельности", examples=["Автомобили", "легковые", "грузовые"])
    parent_id: UUID4 | None = Field(description="Уникальный идентификатор родителя (модет отсутствовать)")
    level: int = Field(default=1, ge=1, le=3, description="Уровень вложенности в дереве (не может превышать 3)", examples=[1,2,3])
