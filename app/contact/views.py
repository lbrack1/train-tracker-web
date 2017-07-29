#app/contact/views.py

from flask import Flask, flash, render_template, request
from forms import ContactForm
from flask.ext.mail import Message, Mail
from . import contact

mail = Mail()


# add contact page route               
@contact.route('/contact',methods=['GET','POST'])
def contactpage():
    form = ContactForm()

    # check form
    if form.validate_on_submit():    
        # if valid tell user and redirect to home page 
        flash('Message Sent! Thank you for getting in touch.')
        msg = Message(form.subject.data, sender='contactform@cryptotracker.co.uk', recipients=['leo.brack@cryptotracker.co.uk'])
        msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)
       # return redirect(url_for('contact'))
    return render_template('contact/contact.html', form=form, title='Contact Us')
