import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}


class User(Base):
    __tablename__ = 'User'
    
    ID = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique=True)
    
    def to_dict(self):
        return {
            "ID": self.ID,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email
        }
    
    
class Follower(Base):
    __tablename__ = 'Follower'
    
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.ID'))
    user_to_id = Column(Integer, ForeignKey('User.ID'))
    def to_dict(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }

class Media(Base):
    __tablename__ = 'Media'
    
    ID = Column(Integer, primary_key=True)
    type = Column(Enum("ejemplo", "ejemplo", "ejemplo"))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('Post.ID'))
    def to_dict(self):
        return {
            "ID": self.ID,
            "post_id": self.post_id,
            "url": self.url,
            "media_type": self.media_type
        }
class Post(Base):
    __tablename__ = 'Post'
    
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.ID'))
    def to_dict(self):
        return {
            "ID": self.ID,
            "user_id": self.user_id
        }
class Comment(Base):
    __tablename__ = 'Comment'
    
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('User.ID')) 
    post_id = Column(Integer, ForeignKey('Post.ID'))
    
    def to_dict(self):
        return {
            "ID": self.ID,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
