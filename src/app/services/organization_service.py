from math import atan2, cos, radians, sin, sqrt

from src.app.repo.building_repo import BuildingRepo
from src.app.repo.organization_repo import OrganizationRepo
from src.app.schemas.area_schema import RadialArea, RectangleArea
from src.app.schemas.organization_schema import OrganizationOut
from src.app.schemas.building_schema import Building


class OrganizationService:
    def __init__(self, building_repo: BuildingRepo, organization_repo: OrganizationRepo):
        self.building_repo = building_repo
        self.organization_repo = organization_repo
    

    def get_organizations_in_radial_area(self, request: RadialArea) -> list[OrganizationOut]:
        buildings: list[Building] = self.building_repo.get_all()
        organizations = []
        
        # Используется формула гаверсинусов
        center_lat_radian = radians(request.center_lat)
        center_lon_radian = radians(request.center_lon)

        for item in buildings:
            building_lat_radian = radians(item.latitude)
            building_lon_radian = radians(item.longitude)

            latitude_diff = center_lat_radian - building_lat_radian
            longitude_diff = center_lon_radian - building_lon_radian

            a = sin(latitude_diff/2)**2 + cos(building_lat_radian) * cos(center_lat_radian) * sin(longitude_diff/2)**2
            c = 2 * atan2(sqrt(a), sqrt(1-a))

            distance = 6371 * c
            if distance <= request.radius:
                organizations.extend(self.organization_repo.get_all_for_current_building(item.id))
        
        return organizations
    
    
    def get_organizations_in_rectangle_area(self, request: RectangleArea) -> list[OrganizationOut]:
        buildings: list[Building] = self.building_repo.get_all()
        organizations = []

        for item in buildings:
            if request.right_bottom_lat <= item.latitude <= request.left_top_lat \
            and request.left_top_lon <= item.longitude <= request.right_bottom_lon:
                organizations.extend(self.organization_repo.get_all_for_current_building(item.id))
        
        return organizations
