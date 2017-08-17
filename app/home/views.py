# app/home/views.py

from flask import render_template
from . import home

# add homepage
@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")
    

