from flask import Blueprint

# admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
admin_bp = Blueprint(
    'admin', 
    __name__, 
    url_prefix='/admin',
    template_folder='../../templates/admin',
    static_folder='../../static/admin',      
    static_url_path='/admin/static'     
)

from . import dashboard
from . import faq