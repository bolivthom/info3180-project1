from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

SECRET_KEY = 'Sup3r$3cretkey'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
UPLOAD_FOLDER = 'app/static/uploads'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project1:password@localhost/project1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

@app.context_processor
def helpers():

    def format_date(date, target_format="%B %d, %Y"):
        # date = datetime.datetime.strptime(value, current_format)
        return date.strftime(target_format)

    return dict(format_date=format_date)

from app import views, models, forms