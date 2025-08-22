from flask import request, jsonify, current_app
import os
from app.models.enquiry_model import EnquiryMdl
from app.controller.api import api_bp
from app.extensions import db
from app.mail import send_email
from app.tasks.send_async_mail import send_async_email
@api_bp.route("/enquiry", methods=['GET', 'POST'])
def Enquiry():
    if request.method == 'GET':
        results = EnquiryMdl.query.filter(EnquiryMdl.status==1).all()
        print("its working")
        if results:
            output = [faq.to_dict() for faq in results]  
            return jsonify({'response': output}), 200
            #return make_response(jsonify([user.json() for user in results]), 200)
        else:
            return jsonify({'msg':'no data available'}), 200


    elif request.method == 'POST':
        try:
            #data = request.get_json() or {}
            data = request.json
            rem_addr = request.remote_addr
            enq = EnquiryMdl(name=data['name'], email=data['email'], contact=data['contact'], desc=data['desc'], rem_addr=rem_addr)
            subject = f"enquiry by {data.get('name')}"
            des = f"""
                name: {data.get('name')},
                email: {data.get('email')},
                contact: {data.get('contact')},
                desc: {data.get('desc')}
            """
            result = send_async_email.delay(subject, "dinesh.sharma11013@gmail.com", des)
            print(result.get(timeout=10))
            #send_email(subject, "dinesh.sharma11013@gmail.com", des)
            db.session.add(enq)
            db.session.commit()
            return jsonify({'message': 'message sent successfully'}), 201
        except Exception as e:
            print("error is", str(e))
            return jsonify({'message': 'error submitting message'}), 500




