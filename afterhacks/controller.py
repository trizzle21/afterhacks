from flask import Flask, render_template
from flask_login import LoginManager
from afterhacks import app



login_manager = LoginManager()

login_manager.init_app(app)



@app.route('/')
def index():
    return render_template('landing.html')








# @app.route('/api/projects')
# def project_dump():


def index():
    return render_template('landing.html')
