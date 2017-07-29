# app/blog/views.py                                                                                                                                                                 
from flask import abort, render_template
from flask_login import current_user, login_required

from . import blog

# add blog  page                                                                                                                                                                    
@blog.route('/blog')
def blogpage():
    return render_template('blog/blog.html', title="Blog")
