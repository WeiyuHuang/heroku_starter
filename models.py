from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = "postgres://qropczofvqeugt:f9bd94fe552b410b223b03391517f8d794d540db73f8d9baefa7b7741cfdd242@ec2-34-202-88-122.compute-1.amazonaws.com:5432/dbkktdu6pq304u"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(db.Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}