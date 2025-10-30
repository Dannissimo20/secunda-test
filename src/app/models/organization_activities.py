from sqlalchemy import UUID, Column, ForeignKey, Table

from src.app.database.database import Base

organization_activities = Table(
    'organization_activities',
    Base.metadata,
    Column('organization_id', UUID(as_uuid=True), ForeignKey('organizations.id'), primary_key=True),
    Column('activity_id', UUID(as_uuid=True), ForeignKey('activities.id'), primary_key=True)
)
