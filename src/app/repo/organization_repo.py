import uuid
from sqlalchemy import select
from src.app.database.database import DBWriter
from src.app.models.activity_model import Activity
from src.app.models.organization_model import Organization
from src.app.schemas.organization_schema import OrganizationOut


class OrganizationRepo:
    def __init__(self, db: DBWriter):
        self.db = db
    

    def get_all(self) -> list[OrganizationOut]:
        query = select(Organization)

        with self.db.session() as session:
            result = session.execute(query).scalars().all()
            return [OrganizationOut.model_validate(item) for item in result]
    

    def get_all_for_current_building(self, building_id: uuid) -> list[OrganizationOut]:
        query = select(Organization).where(Organization.building_id == building_id)

        with self.db.session() as session:
            result = session.execute(query).scalars().all()
            return [OrganizationOut.model_validate(item) for item in result]
    

    def get_all_for_current_activity(self, activity_id: uuid) -> list[OrganizationOut]:
        query = select(Organization).join(Organization.activities).where(Activity.id == activity_id)

        with self.db.session() as session:
            result = session.execute(query).scalars().all()
            return [OrganizationOut.model_validate(item) for item in result]
    

    def get_by_id(self, organization_id: uuid) -> OrganizationOut:
        query = select(Organization).where(Organization.id == organization_id)

        with self.db.session() as session:
            result = session.execute(query).scalars().first()
            return OrganizationOut.model_validate(result) if result is not None else None
        
    
    def get_by_activity_tree(self, activity_id: uuid) -> list[OrganizationOut]:
        activity_cte = (
            select(Activity.id)
            .where(Activity.id == activity_id)
            .cte(name="activity_tree", recursive=True)
        )

        recursive_part = (
            select(Activity.id)
            .join(activity_cte, Activity.parent_id == activity_cte.c.id)
        )
    
        activity_cte = activity_cte.union_all(recursive_part)
        
        query = (
            select(Organization)
            .join(Organization.activities)
            .where(Activity.id.in_(select(activity_cte.c.id)))
            .distinct()
        )

        with self.db.session() as session:
            result = session.execute(query).scalars().all()
            return [OrganizationOut.model_validate(item) for item in result]
    

    def get_by_name(self, organization_name: str) -> OrganizationOut:
        query = select(Organization).where(Organization.name == organization_name)

        with self.db.session() as session:
            result = session.execute(query).scalars().first()
            
            return OrganizationOut.model_validate(result) if result is not None else None
