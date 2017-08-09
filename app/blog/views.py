# app/blog/views.py
                                                                                                                                                                 
from flask import abort, render_template
from flask_login import current_user, login_required

from . import blog

# add blog page                                                                                                                                                                    
@blog.route('/blog')
def blogpage():
    return render_template('blog/blog.html', title="Blog")

# add blog detail page
@blog.route('/blog/detail')
def blogdetail():
    return render_template('blog/detail.html', title="Blog")

# add blog edit page
@blog.route('/blog/edit')
@login_required
def blogedit():
    return render_template('blog/edit.html', title="Edit Blog")
