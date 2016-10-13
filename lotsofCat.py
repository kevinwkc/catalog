from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import  Base, User, Category, Item
from settings import POSTGRES_DB
engine = create_engine(POSTGRES_DB)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

def mockup():
  
  cats = ['Soccer', 'Basketball', 'Baseball', 'Frisbee', 'Snowboarding', 'Rock Climbing', 'Skating', 'Hockey']
  cat = [Category(name = c) for c in cats]

  session.add_all(cat)                
  session.commit()

mockup()