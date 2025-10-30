from pydantic import Field
from src.app.schemas.base_schema import BaseSchema


class RadialArea(BaseSchema):
    center_lat: float = Field(..., ge=-90, le=90, description="Географияческая широта центра", examples=[-90, -40.12345678, 0, 50.6666])
    center_lon: float = Field(..., ge=-180, le=180, description="Географическая долгота центра", examples=[-180, -40.12345678, 0, 50.6666])
    radius: float = Field(..., ge=1, description="Радиус области в километрах", examples=[1, 10, 100, 1000])


class RectangleArea(BaseSchema):
    left_top_lat: float = Field(..., ge=-90, le=90, description="Географическая широта левого верхнего угла области", examples=[-90, -40.12345678, 0, 50.6666])
    left_top_lon: float = Field(..., ge=-180, le=180, description="Географическая долгота левого верхнего угла области", examples=[-180, -40.12345678, 0, 50.6666])
    right_bottom_lat: float = Field(..., ge=-90, le=90, description="Географическая широта правого нижнего угла области", examples=[-90, -40.12345678, 0, 50.6666])
    right_bottom_lon: float = Field(..., ge=-180, le=180, description="Географическая долгота правого нижнего угла области", examples=[-180, -40.12345678, 0, 50.6666])
