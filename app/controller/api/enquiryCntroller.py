from flask import request, jsonify, current_app
import os
from app.models.enquiry_model import EnquiryMdl
from app.controller.api import api_bp


obj = EnquiryMdl()



@api_bp.route('/enquiry', methods=['GET', 'POST'])
def enquiry_controller():
    if request.method == 'GET':
        return obj.get_enquiry()
    
    elif request.method == 'POST':
        print(request.form, request.remote_addr, current_app)
        return obj.save_enquiry(request.form, request.remote_addr)









