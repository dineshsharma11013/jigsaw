from flask import request, jsonify, current_app
import os


from app.controller.api import api_bp



# http://127.0.0.1:5000/api/user
@api_bp.route("/user", methods=['POST', 'GET'])
def user_getall_controller():
    if request.method == 'GET':
        print("sdf")
        return jsonify({'msg': 'Data successfully'}), 200







