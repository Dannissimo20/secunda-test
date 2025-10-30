import uuid
from sqlalchemy import ARRAY, UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.app.database.database import Base
from src.app.models.organization_activities import organization_activities


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4()
    )
    name = Column(String(255), nullable=False)
    phone = Column(ARRAY(String), nullable=False)
    building_id = Column(UUID(as_uuid=True), ForeignKey('buildings.id'), nullable=False)

    building = relationship("Building", back_populates="organizations")
    activities = relationship(
        "Activity",
        secondary=organization_activities,
        back_populates="organizations"
    )
