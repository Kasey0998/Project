import os

class Config:
    SECRET_KEY = 'thisismysecretkey123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///property.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
