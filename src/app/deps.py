from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Singleton, Factory

from src.app.database.database import DBWriter
from src.app.repo.building_repo import BuildingRepo
from src.app.repo.organization_repo import OrganizationRepo
from src.app.services.organization_service import OrganizationService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[".api.organization"]
    )

    db = Singleton(DBWriter)

    organization_repo = Factory(
        OrganizationRepo,
        db=db
    )

    building_repo = Factory(
        BuildingRepo,
        db=db
    )

    organization_service = Factory(
        OrganizationService,
        building_repo=building_repo,
        organization_repo=organization_repo
    )
