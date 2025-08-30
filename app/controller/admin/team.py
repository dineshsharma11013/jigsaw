from flask import render_template
from app.controller.admin import admin_bp
from app.extensions import db
from app.models.team import Team


@admin_bp.route('/team')
def team():
    results = Team.query.order_by(Team.id.desc()).all()
    print("results", results)
    return render_template("admin/team.html", results=results)





