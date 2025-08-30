from flask import Flask, send_from_directory
import os
from dotenv import load_dotenv

from app.filters.filters import register_filters
from app.controller.api import api_bp
from app.controller.admin import admin_bp
from app.extensions import db, migrate, mail
from flask_migrate import Migrate
from app.context_processors import inject_admin_config
from app.celery import celery, init_celery
import redis

load_dotenv()

# Create Flask app
app = Flask(__name__, static_folder=None)

# Load config
basedir = os.path.abspath(os.path.dirname(__file__))
root_dir = os.path.abspath(os.path.join(basedir, '..'))

app.config.from_mapping(
    SECRET_KEY=os.getenv("SECRET_KEY"),
    #SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI"),
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG=True,

    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),

    CELERY=dict(
    broker_url=os.getenv("CELERY_BROKER_URL"),
    result_backend=os.getenv("CELERY_RESULT_BACKEND"),
    task_ignore_result=True,
),

    ADMIN="admin"  # lowercase not allowed if want to use in lowercase then Instead of from_mapping, set it directly:
)

# Initialize Celery
init_celery(app)

# Check Redis
def check_redis_connection():
    try:
        r = redis.Redis.from_url(app.config["CELERY"]["broker_url"])
        r.ping()
        print("✅ Redis is connected!")
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")

check_redis_connection()

# Init extensions
db.init_app(app)
migrate.init_app(app, db)
Migrate(app, db)
mail.init_app(app)

with app.app_context():
    from sqlalchemy.sql import text
    try:
        db.session.execute(text("SELECT 1"))
        print("✅ Database is connected!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    db.create_all()

# Jinja filters
register_filters(app)
app.context_processor(inject_admin_config)

# Blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(api_bp)

# React static
REACT_BUILD = os.path.join(root_dir, "front", "build")
REACT_STATIC = os.path.join(REACT_BUILD, "static")
REACT_ASSETS = os.path.join(REACT_BUILD, "assets")

# backend 
ADMIN_STATIC = os.path.join(root_dir, "app", "static", "admin")
MEDIA_ROOT = os.path.join(root_dir, "app", "media", "uploads")
MEDIA_URL = "/media"

# uploads
UPLOAD_FOLDER = MEDIA_ROOT   
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/static/react/<path:path>")
def serve_react_static(path):
    return send_from_directory(REACT_STATIC, path)

@app.route("/assets/<path:path>")
def serve_react_assets(path):
    return send_from_directory(REACT_ASSETS, path)

@app.route("/static/admin/<path:filename>")
def serve_admin_static(filename):
    return send_from_directory(ADMIN_STATIC, filename)

@app.route(f"{MEDIA_URL}/<path:filename>")
def media_files(filename):
    return send_from_directory(MEDIA_ROOT, filename)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react_app(path):
    file_path = os.path.join(REACT_BUILD, path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory(REACT_BUILD, path)
    else:
        return send_from_directory(REACT_BUILD, "index.html")
