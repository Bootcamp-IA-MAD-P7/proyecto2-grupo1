from pymysql import Timestamp
from sqlalchemy import Column, Date, Float, Integer, String, Numeric, Text, ForeignKey
from database.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship




class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), nullable=False, index=True)
    artist_id = Column(Integer, foreign_key = "artist.id", nullable=False, index=True)
    genre_id = Column(Integer, foreign_key = "genre.id", index=True)
    format_type_id = Column(Integer, foreign_key = "formatType.id", nullable=False, index=True)
    price = Column(Numeric(10, 2), nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    year = Column(Integer, nullable=True)
    image_url = Column(Text(500), nullable=True)
    
    artist = relationship("Artist", back_populates="albums")
    genre = relationship("Genre", back_populates="albums")
    format_type = relationship("formatType", back_populates="albums")
    

class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    nationality = Column(String(45), nullable=False, default=0.0)
    
    albums = relationship("Album", back_populates="artist")

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, unique = True, index=True)
    
    albums = relationship("Album", back_populates="genre")
    
class Product_inventory(Base):
    __tablename__ = "product_inventory"

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, foreign_key="album.id", nullable=False)
    format_type = Column(String(50), nullable=False, index=True)
    barcode = Column(String(45), index=True)
    price = Column(Numeric(10, 2), nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    
    order_details = relationship("OrderDetails", back_populates="product_inventory")
    
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    email = Column(String(45), nullable=False, index=True)
    password_hash = Column(String(45), nullable=False)
    role = Column(String(20), default="customer")
    
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, foreign_key = 'user.id', nullable=False)
    album_id = Column(Integer, foreign_key = 'album.id', nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Numeric(10, 2), nullable=False, default=0.0)
    order_date = Column(Date, nullable=False, default=0)
    order_status = Column(String(20), default="pending")
    
    order_details = relationship("OrderDetails", back_populates="order")
    product_inventory = relationship("Product_inventory", back_populates="order_details")
    user = relationship("User", back_populates="orders")
    
class OrderDetails(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, foreign_key = 'order.id', nullable=False)
    album_id = Column(Integer, foreign_key = 'album.id', nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Numeric(10, 2), nullable=False, default=0.0)

    

class FormatType(Base):
    __tablename__ = "formatType"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    
    
    albums = relationship("Album", back_populates="format_type")
    
    