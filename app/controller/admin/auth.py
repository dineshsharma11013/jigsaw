from flask import render_template, redirect, request, jsonify, url_for
from . import admin_bp

@admin_bp.route('/login')
def login():
    return render_template('admin/login.html')







