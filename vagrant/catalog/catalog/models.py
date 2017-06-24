import json
from datetime import datetime
from flask import jsonify
from flask import session as login_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    """Application user.
    Attributes:
        id (Integer): 
            User ID.
        name (String): 
            User name.
            Usually this includes the user's given name and last name.
        email (String):
            User email.
        picture (String):
            Picture URL.
            The picture may be stored on an external server, for example,
            when using third party authentication.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(256), nullable = False)
    email = Column(String(256), nullable = False)
    picture = Column(String)

    @property
    def serialize(self):
        return {
            'id'           : self.id,
            'name'         : self.name,
            'email'        : self.email,
            'picture'      : self.picture
        }


class Category(Base):
    """Item category.
    Attributes:
        id (Integer): 
            Category ID.
        name (String): 
            Category name.
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = False)

    items = relationship("Item")

    @property
    def serialize(self):
        return {
            'id'            : self.id,
            'name'          : self.name
        }


class Item(Base):
    """Individual item.
    Attributes:
        id (Integer): 
            Item ID.
        name (String): 
            Item name.
        description (String):
            Item description.
        image (String):
            Image file name.
            The actual image is stored on the file system.
        category_id (Integer):
            ID of this item's category.
        category (Category):
            This item's category.
        created (DateTime):
            Date and time when item was created.
        updated (DateTime):
            Date and time of last update.
        user_id (Integer):
            ID of the user who created this item.
        user (User):
            The user who created this item.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = False)
    description = Column(String)
    image = Column(String)
    
    category_id = Column(Integer, ForeignKey("categories.id"), nullable = False)
    category = relationship("Category")
    
    created = Column(DateTime, default = datetime.utcnow)
    updated = Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    user = relationship("User")

    @property
    def serialize(self):
        return {
            'id'            : self.id,
            'name'          : self.name,
            'description'   : self.description,
            'image'         : self.image,
            'category_id'   : self.category_id,
            'user_id'       : self.user_id
        }
