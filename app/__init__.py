from flask import Flask, send_from_directory
import os

from dotenv import load_dotenv
load_dotenv()

from app.filters.filters import register_filters
from app.controller.api import api_bp
from app.controller.admin import admin_bp
from app.extensions import db, migrate, mail
from app.context_processors import inject_admin_config

# Create Flask app and disable default static route
app = Flask(__name__, static_folder=None)

# Load environment and app config
basedir = os.path.abspath(os.path.dirname(__file__))
root_dir = os.path.abspath(os.path.join(basedir, '..'))

app.config.update({
    'TEMPLATES_AUTO_RELOAD': True,
    'SECRET_KEY': os.getenv('SECRET_KEY'),
    'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SEND_FILE_MAX_AGE_DEFAULT': 0,
    'DEBUG': True,
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'admin': 'admin'
})

# Jinja reload support
app.jinja_env.auto_reload = True
app.jinja_env.cache = {}

# Register custom Jinja filters
register_filters(app)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
mail.init_app(app)

# Check DB connection
with app.app_context():
    from sqlalchemy.sql import text
    try:
        db.session.execute(text('SELECT 1'))
        print("✅ Database is connected!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
    db.create_all()

# Register context processor
app.context_processor(inject_admin_config)

# Register Blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(api_bp)

# Directory paths
REACT_BUILD = os.path.join(root_dir, 'front', 'build')
REACT_STATIC = os.path.join(REACT_BUILD, 'static')
REACT_ASSETS = os.path.join(REACT_BUILD, 'assets')
ADMIN_STATIC = os.path.join(root_dir, 'app', 'static', 'admin')


# Serve React static files
@app.route("/static/react/<path:path>")
def serve_react_static(path):
    return send_from_directory(REACT_STATIC, path)

@app.route("/assets/<path:path>")
def serve_react_assets(path):
    return send_from_directory(REACT_ASSETS, path)

# Serve Flask admin static files
@app.route("/static/admin/<path:filename>")
def serve_admin_static(filename):
    return send_from_directory(ADMIN_STATIC, filename)

# Serve React SPA (index.html fallback)
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react_app(path):
    file_path = os.path.join(REACT_BUILD, path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory(REACT_BUILD, path)
    else:
        return send_from_directory(REACT_BUILD, "index.html")
