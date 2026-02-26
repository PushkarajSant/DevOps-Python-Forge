import sys
import os
sys.path.append(os.getcwd())
from database import engine, Base
from models import *
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print('Dropped and recreated!')