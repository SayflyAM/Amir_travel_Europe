from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

# Singletons shared across the app

db = SQLAlchemy()
babel = Babel()
