from flask import request, jsonify, current_app, make_response
import os
from app.models.faq import FAQ
from app.controller.api import api_bp


#https://dev.to/francescoxx/build-a-crud-rest-api-in-python-using-flask-sqlalchemy-postgres-docker-28lo

@api_bp.route("/faq", methods=['GET'])
def getFaq():
    if request.method == 'GET':
        results = FAQ.query.filter(FAQ.status==1).all()
        if results:
            faqs = [faq.to_dict() for faq in results]  
            return jsonify({'response': faqs})
            #return make_response(jsonify([user.json() for user in results]), 200)
        else:
            return jsonify({'msg':'no data available'}), 200














