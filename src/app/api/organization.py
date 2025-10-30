from fastapi import APIRouter, Depends
from pydantic import UUID4
from dependency_injector.wiring import inject, Provide

from src.app.repo.organization_repo import OrganizationRepo
from src.app.schemas.area_schema import RadialArea, RectangleArea
from src.app.schemas.organization_schema import OrganizationOut
from src.app.deps import Container
from src.app.services.organization_service import OrganizationService


organization_router = APIRouter(
    prefix="/organization",
    tags=['Organization - управление организациями'],
)


@organization_router.get(
    "/get-all", 
    response_model=list[OrganizationOut],
    summary="Получить все организации",
    description="Возвращает список всех организаций в системе",
    
)
@inject
def get_all(organization_repo: OrganizationRepo = Depends(Provide[Container.organization_repo])):
    """
    Получить все организации
    
    Возвращает полный перечень всех зарегистрированных в системе организаций
    с их основной информацией.
    
    **Возвращает:** 
    - List[OrganizationOut] - список организаций в здании
    - Может вернуть пустой список, если организации в здании отсутствуют
    """
    return organization_repo.get_all()


@organization_router.get(
    "/get-in-current-building", 
    response_model=list[OrganizationOut],
    summary="Получить все организации в здании",
    description="Возвращает список всех организаций, находящихся в конкретном здании",
)
@inject
def get_all_in_current_building(building_id: UUID4, organization_repo: OrganizationRepo = Depends(Provide[Container.organization_repo])):
    """
    Получить все организации в выбраном здании
    
    Возвращает полный перечень всех организаций в указаном здании.

    **Параметры:**
    - *building_id* (UUID): Уникальный идентификатор здания (обязательный)
    
    **Возвращает:** 
    - List[OrganizationOut] - список организаций в здании
    - Может вернуть пустой список, если организации в здании отсутствуют
    """
    return organization_repo.get_all_for_current_building(building_id)


@organization_router.get(
    "/get-for-current-activity", 
    response_model=list[OrganizationOut],
    summary="Получить все организации с определённым видом деятельности",
    description="Возвращает список всех организаций, занимающихся определённым видом деятельности",
)
@inject
def get_all_for_current_activity(activity_id: UUID4, organization_repo: OrganizationRepo = Depends(Provide[Container.organization_repo])):
    """
    Получить все организации с определённым видом деятельности
    
    Возвращает полный перечень всех организаций занимающихся указанным видом деятельности.

    **Параметры:**
    - *activity_id* (UUID): Уникальный идентификатор деятельности (обязательный)
    
    **Возвращает:** 
    - List[OrganizationOut]: список организаций в здании
    - Может вернуть пустой список, если организации занимающиеся данной деятельностью отсутствуют
    """
    return organization_repo.get_all_for_current_activity(activity_id)


@organization_router.post(
    "/get-in-radial-area", 
    response_model=list[OrganizationOut],
    summary="Поиск организаций в круговой области",
    description="Возвращает список всех организаций, находящихся в пределах заданной круговой области на карте",
)
@inject
def get_all_for_radial_area(request: RadialArea, organization_service: OrganizationService = Depends(Provide[Container.organization_service])):
    """
    Поиск организаций в круговой области по координатам

    Выполняет поиск всех организаций, находящихся в пределах круговой области с заданным центром и радиусом.

    **Параметры:**
    - *center_lat* (float): Широта центра области (от -90 до 90) (обязательный)
    - *center_lon* (float): Долгота центра области (от -180 до 180) (обязательный) 
    - *radius* (float): Радиус поиска в километрах (≥ 1) (обязательный)

    **Пример запроса:**
    ```json
    {
        "center_lat": 55.7558,
        "center_lon": 37.6173,
        "radius": 5.0
    }
    ```

    **Возвращает:**
    - List[OrganizationOut]: список организаций в указанной области
    - Пустой список, если организации не найдены в заданном радиусе
    """
    return organization_service.get_organizations_in_radial_area(request)


@organization_router.post(
    "/get-in-rectangle-area", 
    response_model=list[OrganizationOut],
    summary="Поиск организаций в прямоугольной области",
    description="Возвращает список всех организаций, находящихся в пределах заданной прямоугольной области на карте",
)
@inject
def get_all_for_rectangle_area(request: RectangleArea, organization_service: OrganizationService = Depends(Provide[Container.organization_service])):
    """
    Поиск организаций в прямоугольной области по координатам

    Выполняет поиск всех организаций, находящихся в пределах прямоугольной области,
    заданной координатами левого верхнего и правого нижнего углов.

    **Параметры:**
    - *left_top_lat* (float): Широта левого верхнего угла области (от -90 до 90) (обязательный)
    - *left_top_lon* (float): Долгота левого верхнего угла области (от -180 до 180) (обязательный)
    - *right_bottom_lat* (float): Широта правого нижнего угла области (от -90 до 90) (обязательный)
    - *right_bottom_lon* (float): Долгота правого нижнего угла области (от -180 до 180) (обязательный)

    **Пример запроса:**
    ```json
    {
        "left_top_lat": 55.7700,
        "left_top_lon": 37.6000,
        "right_bottom_lat": 55.7300,
        "right_bottom_lon": 37.6500
    }
    ```

    **Возвращает:**
    - List[OrganizationOut]: список организаций в указанной области
    - Пустой список, если организации не найдены в заданной области
    """
    return organization_service.get_organizations_in_rectangle_area(request)


@organization_router.get(
    "/get-by-id", 
    response_model=OrganizationOut | None,
    summary="Поиск организации по идентификатору",
    description="Возвращает организацию по ее уникальному идентификатору"
)
@inject
def get_organization_by_id(organization_id: UUID4, orgnization_repo: OrganizationRepo = Depends(Provide[Container.organization_repo])):
    """
    Получить организацию по идентификатору

    Возвращает полную информацию об организации по ее уникальному идентификатору.

    **Параметры:**
    - *organization_id* (UUID4): Уникальный идентификатор организации (обязательный)

    **Возвращает:**
    - OrganizationOut | None: объект организации, если найдена
    - None, если организация с указанным идентификатором не существует
    """
    return orgnization_repo.get_by_id(organization_id)


@organization_router.get(
    "/all-by-activity-tree", 
    response_model=list[OrganizationOut],
    summary="Поиск организаций по дереву деятельности",
    description="Возвращает список организаций, связанных с указанной деятельностью",
)
@inject
def get_all_by_activity_tree(activity_id: UUID4, organization_repo: OrganizationRepo = Depends(Provide[Container.organization_repo])):
    """
    Получить организации по дереву деятельности

    Возвращает все организации, которые связаны с указанной деятельностью 
    или любыми дочерними деятельностями в иерархии.

    **Параметры:**
    - *activity_id* (UUID4): Уникальный идентификатор корневой деятельности (обязательный)

    **Возвращает:**
    - List[OrganizationOut]: список организаций, связанных с указанным деревом деятельности
    - Пустой список, если организации не найдены для данной деятельности
    """
    return organization_repo.get_by_activity_tree(activity_id)


@organization_router.get(
    "/get_by_name", 
    response_model=OrganizationOut | None,
    summary="Поиск организации по названию",
    description="Возвращает организацию по точному совпадению названия",
)
@inject
def get_organization_by_name(organization_name: str, organization_repo: OrganizationRepo = Depends(Provide[Container.organization_repo])):
    """
    Получить организацию по названию

    Выполняет поиск организации по точному совпадению названия.
    Поиск чувствителен к регистру и требует точного совпадения.

    **Параметры:**
    - *organization_name* (str): Название организации для поиска (обязательный)

    **Возвращает:**
    - OrganizationOut | None: объект организации, если найдена
    - None, если организация с указанным названием не существует

    **Примечание:**
    - Поиск выполняется по точному совпадению названия
    """
    return organization_repo.get_by_name(organization_name)
