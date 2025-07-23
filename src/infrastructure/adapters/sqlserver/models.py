# src/infrastructure/database/models.py
from sqlalchemy import Column, String, Boolean, DateTime, LargeBinary, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

# 1. Create a Base class that all your models will inherit from.
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # Store only hashed passwords
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"




class ChartImage(Base):
    __tablename__ = 'chart_images'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    image_data = Column(LargeBinary, nullable=False)  # For storing binary data
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    analyses = relationship("ChartAnalysis", back_populates="chart_image")
    
    def __repr__(self):
        return f"<ChartImage(id={self.id}, user_id={self.user_id})>"

class ChartAnalysis(Base):
    __tablename__ = 'chart_analyses'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chart_image_id = Column(UUID(as_uuid=True), ForeignKey('chart_images.id'), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    chart_image = relationship("ChartImage", back_populates="analyses")
    
    def __repr__(self):
        return f"<ChartAnalysis(id={self.id}, chart_image_id={self.chart_image_id})>"