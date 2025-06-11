from flask import render_template, redirect, request, jsonify, url_for
from app.controller.admin import admin_bp
from app.models.faq import FAQ
from app.extensions import db



@admin_bp.route("/faq")
def faq():
    results = FAQ.query.order_by(FAQ.id.desc()).all()
    print("results", results)
    return render_template("admin/faq.html", results=results)

@admin_bp.route("/add-faq", methods=['GET', 'POST'])
def addFaq():
    if request.method=='POST':
        try:
            title = request.form.get('title')
            desc = request.form.get('descptn', '')
            status = request.form.get('status')
            rem_addr = request.remote_addr 
            res = FAQ(title=title, desc=desc, status=status, rem_addr=rem_addr)
            db.session.add(res)
            db.session.commit()
            #print("title", title)
            return jsonify({'error':False, 'message':'Data saved successfully'})
        except Exception as e:
            print("title", str(e))
            return jsonify({'error':True, 'message':str(e)})        
        
    return render_template("admin/addFaq.html") 

@admin_bp.route("/update-faq/<int:id>", methods=['GET', 'POST', 'DELETE'])
def updateFaq(id):
    cat = FAQ.query.filter_by(id=id).first()
    if not cat:
        return redirect(url_for('admin_bp.faq'))
    if request.method == 'POST':
        cat.title = request.form.get('title')
        cat.desc = request.form.get('descptn', '')
        cat.status = request.form.get('status')
        try:
            cat.rem_addr = request.remote_addr 
            db.session.commit()
            #print("title", title)
            return jsonify({'error':False, 'message':'Data saved successfully'})
        except Exception as e:
            print("title", str(e))
            #db.session.rollback()  # Rollback any changes in case of error
            return jsonify({'error':True, 'message':str(e)})     
    
    if request.method == 'DELETE':
        try:
            db.session.delete(cat)
            db.session.commit()
            return jsonify({'error':False, 'message':'Data deleted successfully'})
        except Exception as e:   
            print("error", str(e))
            #db.session.rollback()  # Rollback any changes in case of error
            return jsonify({'error':True, 'message':str(e)}) 
    return render_template("admin/editFaq.html", cat=cat)











