from flask import render_template, redirect, request, jsonify, url_for
from . import admin_bp

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

