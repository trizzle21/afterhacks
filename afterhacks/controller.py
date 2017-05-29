""" Controller that controls routes

"""
from flask import render_template, redirect, url_for
from afterhacks import app

from .forms import EmailPasswordForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('landing.html')



@app.route('/login', methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():


        return redirect(url_for('index'))
    return render_template('login.html', form=form)


# @app.route('/api/projects')
# def project_dump():
