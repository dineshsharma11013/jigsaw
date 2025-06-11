from app.models import cur, con
from datetime import datetime
from flask import jsonify, current_app
import os
from app.helper import Helper
from datetime import datetime
from app.mail import send_email

hl = Helper()

class EnquiryMdl():
    def __init__(self):
        try:
            #mysql.connector.connect(host="localhost", user="root", password="", database="flask_tutorial2")
            current_time = datetime.now()
            self.formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            print("connected successfully")
        except Exception as e:
            print("error - ",e)
            
            
    def get_enquiry(self):
        try:
            #cur.execute(f"select * from enquiry_mdl")
            #cur.fetchall()
            data = hl.getAllData('enquiry_mdl') 
            print(data)
            if len(data) > 0:
                return jsonify({'payload':data}), 200
            else:
                return jsonify({'msg':'There is no data.'}), 204
        except Exception as e:
            print("error - ",e)
            return jsonify({'error': 'Failed to fetch data'}), 500            
        
        
    def save_enquiry(self, data, rem_addr):
        try:
            query = "INSERT INTO enquiry_mdl (name, email, phone, subject, message, rem_addr, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (data['name'], data['email'], data['phone'], data['subject'], data['message'], rem_addr, datetime.now()))
            send_email("test", "dinesh.sharma11013@gmail.com", "hello world")
            return jsonify({'msg': 'Message sent successfully'}), 201         
        except Exception as e:
            print("Error:", e)
            return jsonify({'error': 'Failed to save data'}), 500         
        
        
        
        