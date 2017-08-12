# app/home/views.py

from flask import abort, render_template, make_response
from flask_login import current_user, login_required
import MySQLdb

#TEST
import json
from time import time
from random import random
#

from . import home

# add homepage
@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

# add user dashboard. Login needed
@home.route('/dashboard')
@login_required
def dashboard():

    # Get twitter data
#    text = get_data(5)

    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

@home.route('/dashboard/live-data')
def live_data():
    
    # Open a database connection
    #connection = MySQLdb.connect (host = "localhost", user = "leobrack", passwd = "password", db = "crypto_db")

    # Prepare a cursor object using cursor() method
    #cursor = connection.cursor ()
    
    #Get last x seconds of tweets from mysql
   # nowtime = datetime.datetime.now()
   # prevtime = nowtime - datetime.timedelta(seconds=x)
   # nowtimestr = nowtime.strftime('%Y-%m-%d %H:%M:%S.%f')
   # prevtimestr = prevtime.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Execute the SQL query using execute() method.
    #cursor.execute ("select text from twitter where created_at between '" + nowtimestr + "' and '" + prevtimestr + "';")

    # FOR DEVELOPMENT! Execute the SQL query using execute() method.
    #cursor.execute ("select id from twitter where created_at between '2017-08-09 09:59:30' and '2017-08-11 13:50:32';")

    # Fetch all of the rows from the query
    #id  = cursor.fetchall ()
        
    # Close the cursor object
    #cursor.close ()

    # Close the connection
    #connection.close ()


    #################################TEST########################


    # Create a PHP array and echo it as JSON
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

   # return id
    

