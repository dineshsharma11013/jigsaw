from flask import request, jsonify, current_app
import os
from app.models.blog_model import BlogMdl
from app.controller.api import api_bp

obj = BlogMdl()



@api_bp.route('/blogs', methods=['GET', 'POST'])
def blogCntrlr():
    if request.method == 'GET':
        return obj.getBlogs()
    
    elif request.method == 'POST':
        #print(request.form, request.remote_addr, request.files)
        return obj.save_blog(request.form, request.remote_addr, request.files)



@api_bp.route('/blogs/<id>', methods=['GET', 'POST', 'DELETE'])
def blogDetailCntrlr(id):
    if request.method == 'GET':
        return obj.getSelectedData(id)

    elif request.method == 'POST':
        return obj.updateSelectedData(request.form, request.remote_addr, request.files, id)

    elif request.method == 'DELETE':
        return obj.deleteSelected(id)    






