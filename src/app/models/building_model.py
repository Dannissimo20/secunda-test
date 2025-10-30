import uuid
from sqlalchemy import UUID, Column, Numeric, String
from sqlalchemy.orm import relationship
from src.app.database.database import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default = uuid.uuid4()
    )
    address = Column(String(1023))
    latitude = Column(Numeric(10, 8), nullable=False)
    longitude = Column(Numeric(11, 8), nullable=False)

    organizations = relationship("Organization", back_populates="building")
