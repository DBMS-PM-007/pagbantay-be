from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
import uuid

Base = declarative_base()

# Admin Access Model
class AdminAccess(Base):
    __tablename__ = "Admin Access"

    admin_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("User.user_id"), nullable=False)

    # Relationship to the User model
    user = relationship("User", back_populates="admin_access")
    event = relationship("Event", back_populates="admin_access")

# User Model
class User(Base):
    __tablename__ = "User"

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    is_admin = Column(Boolean, default=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)
    status = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)

    # Relationship to Admin Access (One-to-One)
    admin_access = relationship("AdminAccess", back_populates="user", uselist=False)
    availability = relationship("Availability", back_populates="user")
    assignments = relationship("VolunteerAssignment", back_populates="user")

# Volunteer Assignment Model
class VolunteerAssignment(Base):
    __tablename__ = "Volunteer Assignment"

    assignment_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String, ForeignKey("Event.event_id"), nullable=False)
    user_id = Column(String, ForeignKey("User.user_id"), nullable=False)
    station = Column(String, nullable=False)
    shift_start_time = Column(DateTime, nullable=False)
    shift_end_time = Column(DateTime, nullable=False)
    availability_status = Column(String, nullable=False)

    # Relationships
    user = relationship("User", back_populates="assignments")
    event = relationship("Event")

# Event Model
class Event(Base):
    __tablename__ = "Event"

    event_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    admin_id = Column(String, ForeignKey("Admin Access.admin_id"), nullable=False)
    event_name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Relationships
    admin_access = relationship("AdminAccess", back_populates="event")
    availability = relationship("Availability", back_populates="event")

# Availability Model
class Availability(Base):
    __tablename__ = "Availability"

    availability_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("User.user_id"), nullable=False)
    event_id = Column(String, ForeignKey("Event.event_id"), nullable=False)
    station_assignment = Column(String, nullable=False)
    availability = Column(String, nullable=False)

    # Relationships
    user = relationship("User", back_populates="availability")
    event = relationship("Event", back_populates="availability")

   
