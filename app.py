import routes
from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
# TODO: read this from environ but do we *really* need it? ehh....
app.config['SECRET_KEY'] = 'A secret'

all_methods = ['GET', 'POST']

# Home page (where you will add a new user)
app.add_url_rule('/', view_func=routes.index)
# "Thank you for submitting your form" page
app.add_url_rule('/submitted', methods=all_methods, view_func=routes.submitted)
# Viewing all the content in the database page

# probs dont' need this anymore huh. oh well
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # no warning messages

