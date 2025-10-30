import uuid
from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.app.database.database import Base
from src.app.models.organization_activities import organization_activities


class Activity(Base):
    __tablename__ = 'activities'

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4()
    )
    name = Column(String(255), nullable=False)
    parent_id = Column(ForeignKey('activities.id'), nullable=True)
    level = Column(Integer, nullable=False, default=1)

    children = relationship(
        "Activity",
        backref="parent",
        remote_side=[id]
    )

    organizations = relationship(
        "Organization",
        secondary=organization_activities,
        back_populates="activities"
    )
