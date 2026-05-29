from pymysql import Timestamp
from sqlalchemy import Column, Date, Float, Integer, String, Numeric, Text
from database.database import Base

class Album(Base):
    __tablename__ = "album"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), nullable=False, index=True)
    artist_id = Column(String(45), foreign_key = "artist.id", nullable=False, index=True)
    genre_id = Column(String(45), foreign_key = "genre.id", index=True)
    price = Column(Float(10, 2), nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    year = Column(Integer, nullable=True)
    format = Column(String(50), index=True)
    image_url = Column(Text(500), nullable=True)


class Artist(Base):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    biography = Column(Text(500), index=True)
    nationality = Column(String(45), nullable=False, default=0.0)
    created_at = Column(Timestamp, nullable=False, default=0)

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, unique = True, index=True)
    
class Product_inventory(Base):
    __tablename__ = "product_inventory"

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, foreign_key="album.id", nullable=False)
    format_type = Column(String(50), nullable=False, index=True)
    barcode = Column(String(45), index=True)
    price = Column(Float(10, 2), nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    
    
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    email = Column(String(45), nullable=False, index=True)
    password_hash = Column(String(45), nullable=False)
    role = Column(String(20), default="customer")

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, foreign_key = 'user.id', nullable=False)
    album_id = Column(Integer, foreign_key = 'album.id', nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Float,(10, 2), nullable=False, default=0.0)
    order_date = Column(Date, nullable=False, default=0)
    order_status = Column(String(20), default="pending")
    
class order_details(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, foreign_key = 'orders.id', nullable=False)
    album_id = Column(Integer, foreign_key = 'album.id', nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float(10, 2), nullable=False, default=0.0)

