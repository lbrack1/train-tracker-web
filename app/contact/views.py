from flask import Flask, flash, render_template, request
from forms import ContactForm

from . import contact

# add contact page route                                                                                                                                                             
@contact.route('/contact',methods=['GET','POST'])
def contactpage():
    form = ContactForm()

    # check form
    if form.validate_on_submit():    
        # if valid tell user and redirect to home page 
        flash('Message Sent! Thank you for getting in touch.')
       # return redirect(url_for('contact'))
    return render_template('contact/contact.html', form=form, title='Contact Us')
