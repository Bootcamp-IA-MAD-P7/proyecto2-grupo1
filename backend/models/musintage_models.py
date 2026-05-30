# models/musintage_models.py

from sqlalchemy import Column, Date, Integer, String, Numeric, Text, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), nullable=False, index=True)
    artist_id = Column(Integer, ForeignKey("artist.id"), nullable=False, index=True)
    genre_id = Column(Integer, ForeignKey("genre.id"), index=True)
    format_type_id = Column(Integer, ForeignKey("format_type.id"), nullable=False, index=True)
    price = Column(Numeric(10, 2), nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    year = Column(Integer, nullable=True)
    image_url = Column(Text(500), nullable=True)
    
    # Relaciones
    artist = relationship("Artist", back_populates="albums")
    genre = relationship("Genre", back_populates="albums")
    format_type = relationship("FormatType", back_populates="albums") 

class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    nationality = Column(String(45), nullable=False)
    
    # Relación
    albums = relationship("Album", back_populates="artist")

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, unique=True, index=True)
    
    # Relación
    albums = relationship("Album", back_populates="genre")

class FormatType(Base):
    """Tabla catálogo de formatos"""
    __tablename__ = "format_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    
    # Relación con Album
    albums = relationship("Album", back_populates="format_type")
    
#### Tabla User ####

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    email = Column(String(45), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)  # Aumentado para hash seguro
    role = Column(String(20), default="customer")
    
    # Relaciones
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    order_date = Column(Date, nullable=False, default=func.current_date())
    order_status = Column(String(20), default="pending")
    total_amount = Column(Numeric(10, 2), nullable=False, default=0.0)
    
    # Relaciones
    user = relationship("User", back_populates="orders")
    details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    album_id = Column(Integer, ForeignKey("album.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Numeric(10, 2), nullable=False, default=0.0)
    
    # Relaciones
    order = relationship("Order", back_populates="details")
    album = relationship("Album")  # Relación con Album existente