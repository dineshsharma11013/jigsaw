from flask import current_app

def inject_admin_config():
    #print("current_app", current_app)
    return dict(admin_url=current_app.config['admin'])



