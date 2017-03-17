from flask import Flask, render_template
from afterhacks import app

@app.route('/')
def index():
    return render_template('landing.html')








# @app.route('/api/projects')
# def project_dump():
