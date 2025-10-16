from flask import render_template, request, jsonify, url_for, redirect, current_app
from app.controller.admin import admin_bp
from app.extensions import db
from app.models.team import Team
from app.helper import Helper
import os

hl = Helper()

@admin_bp.route('/team')
def team():
    results = Team.query.order_by(Team.id.desc()).all()
    print("results", results)
    return render_template("admin/team.html", results=results)

@admin_bp.route('/add-team', methods=['GET', 'POST'])
def addTeam():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            profile = request.form.get('profile', '')
            status = request.form.get('status')
            rem_addr = request.remote_addr

            img_path = current_app.config['UPLOAD_FOLDER']
            fl = request.files['file']
            if fl:
                filename = hl.make_unique(fl.filename)
                save_path = os.path.join(img_path, 'team', filename)
                fl.save(save_path)
            else:
                filename = ''   

            res = Team(name=name, profile=profile, file_path=filename, status=status, rem_addr=rem_addr)
            db.session.add(res)
            db.session.commit()
            #print("title", title)
            return jsonify({'error':False, 'message':'Data saved successfully'})
        except Exception as e:
            print("title", str(e))
            return jsonify({'error':True, 'message':str(e)})        
        
    return render_template("admin/addTeam.html") 


@admin_bp.route('/edit-team/<int:id>', methods=['GET', 'POST'])
def editTeam():
    cat = Team.query.filter_by(id=id).first()
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            profile = request.form.get('profile', '')
            status = request.form.get('status')
            rem_addr = request.remote_addr

            img_path = current_app.config['file_dir']
            fl = request.files['file']
            if fl:
                filename = hl.make_unique(fl.filename)
                save_path = os.path.join(img_path, 'uploads', 'team', filename)
                fl.save(save_path)
            else:
                filename = ''   

            res = Team(name=name, profile=profile, file_path=filename, status=status, rem_addr=rem_addr)
            db.session.add(res)
            db.session.commit()
            #print("title", title)
            return jsonify({'error':False, 'message':'Data saved successfully'})
        except Exception as e:
            print("title", str(e))
            return jsonify({'error':True, 'message':str(e)})        
        
    return render_template("admin/addTeam.html", cat=cat) 










