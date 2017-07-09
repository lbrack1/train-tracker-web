# run.py

import os
from flask.ext.mail import Mail
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

mail = Mail()

app.config["MAIL_SERVER"] = "smtp.zoho.eu"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contactform@cryptotracker.co.uk'
app.config["MAIL_PASSWORD"] = 'Contactform'

mail.init_app(app)

if __name__ == '__main__':
    app.run()
