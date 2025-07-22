# src/infrastructure/database/models.py
from sqlalchemy import Column, String, Boolean, DateTime, LargeBinary, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER  # For SQL Server UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# 1. Create a Base class that all your models will inherit from.
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=func.newid())
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # Store only hashed passwords
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"




class ChartImage(Base):
    __tablename__ = 'chart_images'
    
    id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=func.newid())
    user_id = Column(UNIQUEIDENTIFIER, ForeignKey('users.id'), nullable=False)
    image_data = Column(LargeBinary, nullable=False)  # For storing binary data
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    analyses = relationship("ChartAnalysis", back_populates="chart_image")
    
    def __repr__(self):
        return f"<ChartImage(id={self.id}, user_id={self.user_id})>"

class ChartAnalysis(Base):
    __tablename__ = 'chart_analyses'
    
    id = Column(UNIQUEIDENTIFIER, primary_key=True, server_default=func.newid())
    chart_image_id = Column(UNIQUEIDENTIFIER, ForeignKey('chart_images.id'), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship
    chart_image = relationship("ChartImage", back_populates="analyses")
    
    def __repr__(self):
        return f"<ChartAnalysis(id={self.id}, chart_image_id={self.chart_image_id})>"