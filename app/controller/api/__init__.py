from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api')


from . import faqCntrlr
# from . import admin_controller
from . import enquiryCntroller
# from . import blogCntrlr

