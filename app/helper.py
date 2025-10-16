from flask import jsonify, current_app
from uuid import uuid4
import os
import re

class Helper():
        def make_unique(self, filename):
                ident = uuid4().__str__()
                extension = filename.split('.')[-1]
                return f"{ident}.{extension}"
    
