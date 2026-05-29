from sqlalchemy import Column, Float, Integer, String, Numeric, Text
from database.database import Base

class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), nullable=False, index=True)
    artist = Column(String(45), nullable=False, index=True)
    genre = Column(String(45), index=True)
    price = Column(Float(10, 2), nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    year = Column(Integer, nullable=True)
    format = Column(String(50), index=True)
    image_url = Column(Text(500), nullable=True)
    
class Artists(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    biography = Column(Text(500), index=True)
    nationality = Column(Numeric(10, 2), nullable=False, default=0.0)
    created_at = Column(Integer, nullable=False, default=0)

class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    
class Product_inventory(Base):
    __tablename__ = "product_inventory"

    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, nullable=False)
    format_tupe = Column(String(50), index=True)
    barcade = Column(String(45), nullable=False, index=True)
    price = Column(Float(10, 2), nullable=False, default=0.0)
    stock = Column(Integer, nullable=False, default=0)
    
    

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False, index=True)
    email = Column(String(45), nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(20), nullable=False, default="customer")

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    album_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Integer(10, 2), nullable=False, default=0.0)
    order_date = Column(Integer, nullable=False, default=0)
    order_status = Column(String(20), nullable=False, default="pending")
    
class order_details(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    album_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Integer(10, 2), nullable=False, default=0.0)

