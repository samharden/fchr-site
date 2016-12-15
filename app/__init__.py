from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy as sa

app = Flask(__name__)
app.config.from_object('config')


from app import views, models
