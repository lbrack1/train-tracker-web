from __future__ import division
# app/dashboard/views.py

from flask import abort, render_template, make_response, jsonify
from flask_login import current_user, login_required
import MySQLdb
import datetime


#TEST
import json
from time import time
from random import random
#

from . import dashboard as dashb

# add user dashboard. Login needed
@dashb.route('/dashboard')
@login_required
def dashboard():

    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('dashboard/dashboard.html', title="Dashboard")

# add admin dashboard view
@dashb.route('/dashboard/admin')
@login_required
def admin_dashboard():
#    prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('dashboard/admin_dashboard.html', title="Dashboard")

@dashb.route('/dashboard/account')
@login_required
def dashboard_account():
    return render_template('dashboard/account.html', title="Account")

@dashb.route('/dashboard/activity/btc')
@login_required
def dashboard_activity_btc():
    return render_template('dashboard/activity/btc_activity.html', title="Btc")

@dashb.route('/dashboard/price/btc')
@login_required
def dashboard_price_btc():
    return render_template('dashboard/price/btc_price.html', title="Btc")

@dashb.route('/dashboard/sentiment/btc')
@login_required
def dashboard_sentiment():
    return render_template('dashboard/sentiment/btc_sentiment.html', title="Btc")

# add page to route data
@dashb.route('/dashboard/activity/live-data')
@login_required
def live_data():
    
    # Open a database connection
    connection = MySQLdb.connect (host = "localhost", user = "leobrack", passwd = "password", db = "crypto_db")

    # Prepare a cursor object using cursor() method
    cursor = connection.cursor ()
    
    #Get last x seconds of tweets from mysql
    now_time = time()*1000 #record time for plot (datetime format not json serializable)
    start = datetime.datetime.now() - datetime.timedelta(seconds = 30)
    end = datetime.datetime.now()    
    # Execute the SQL query using execute() method.
    query = ("select text from raw_tweets where created_at between %s and %s ")
    cursor.execute(query, (start,end))

    # Fetch all of the rows from the query
    try:
        # Data returned as tuple so must be unpacked
        tweets  = cursor.fetchall()
        num_tweets = len(tweets)
        tps = num_tweets/30

    # Due to time scnychronisity errors, sometimes no data is returned
    # To prevent the script crashing, tps value manually set to zero
    except TypeError:
        tps = 0.0
        
    data = [now_time,tps]

    # Close the cursor object
    cursor.close ()

    # Close the connection
    connection.close ()

    # Echo data as JSON
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

    #################################TEST########################


    # Create a PHP array and echo it as JSON
    #data = [time() * 1000, random() * 100]
    #response = make_response(json.dumps(data))
    #response.content_type = 'application/json'
    #return response





