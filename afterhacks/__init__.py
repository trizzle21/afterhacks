# CopyLeft 2017
#
# 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)


app.config.from_object('config')
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)


from flask_assets import Environment, Bundle

# assets = Environment(app)
# assets.url = app.static_url

# scss = Bundle(
# 	scss='css/style.scss',
# 	depends='**/*.scss',
#     filters=('pyscss',),
#     output='all.css'
# )


from afterhacks import controller, models

