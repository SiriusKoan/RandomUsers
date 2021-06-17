# It is still under testing
import RandomUsers as ru
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class User(base):
    __tablename__ = "users"
    ID = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

engine = create_engine("sqlite:///data.db")
base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()

username = ru.Username()
password = ru.Password()
email = ru.Email()
user_model = ru.BasicModel(username=username, password=password, email=email, instance=User)
user = user_model.generate()
session.add(user)
session.commit()
