from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# Admin Access Model
class AdminAccess(Base):
    __tablename__ = "Admin Access"

    admin_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)

    # Relationship to the User model
    user = relationship("User", back_populates="admin_access")

# User Model
class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    is_admin = Column(Boolean, default=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)
    status = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)

    # Relationship to Admin Access (One-to-One)
    admin_access = relationship("AdminAccess", back_populates="user", uselist=False)

# Notification Model
class Notification(Base):
    __tablename__ = "Notification"

    notification_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    message = Column(String, nullable=False)
    status = Column(String, nullable=False)

# Volunteer Assignment Model
class VolunteerAssignment(Base):
    __tablename__ = "Volunteer Assignment"

    assignment_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("Event.event_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    station = Column(String, nullable=False)
    shift_start_time = Column(DateTime, nullable=False)
    shift_end_time = Column(DateTime, nullable=False)
    availability_status = Column(String, nullable=False)

    # Relationships to User and Event models
    user = relationship("User")
    event = relationship("Event")

# Event Model
class Event(Base):
    __tablename__ = "Event"

    event_id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey("Admin Access.admin_id"), nullable=False)
    event_name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Relationship to AdminAccess model
    admin_access = relationship("AdminAccess")

    # Relationship to Event model
    events = relationship("Event", back_populates="event")

