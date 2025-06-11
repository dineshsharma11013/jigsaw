from flask import Flask, render_template
import os
from app.filters.filters import register_filters
from app.controller.api import api_bp
from app.controller.admin import admin_bp
#from flask_mail import Mail
#from flask_caching import Cache

from sqlalchemy.sql import text
from dotenv import load_dotenv
load_dotenv()

from app.extensions import db, migrate, mail

port = 5000
app = Flask(__name__)


app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
app.jinja_env.cache = {}
register_filters(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['file_dir'] = os.path.join(basedir, 'static').replace('\\','/')


app.config['TEMPLATES_AUTO_RELOAD'] = True  
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
app.config['admin'] = "admin"
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dinesh.sharma11013@gmail.com'
app.config['MAIL_PASSWORD'] = 'dscffkjdccnlimlz'
#app.config['MAIL_DEFAULT_SENDER'] = 'your-email@example.com'
#app.config['CACHE_TYPE'] = 'null'
#cache = Cache(app)

db.init_app(app)
migrate.init_app(app, db)
with app.app_context():
        try:
            db.session.execute(text('SELECT 1'))
            print("✅ Database is connected!")
        except Exception as e:
            print(f"❌ Database connection failed: {str(e)}")

        db.create_all()   


mail.init_app(app) 

from app.context_processors import inject_admin_config
app.context_processor(inject_admin_config)

#from app import mail  

app.register_blueprint(admin_bp)
app.register_blueprint(api_bp)

# @app.route('/')
# def home():
#     return render_template('test.html')

# @app.route('/')
# def home():
#     return render_template('.html')

