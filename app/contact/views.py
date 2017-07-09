from flask import Flask, render_template, request
from forms import ContactForm

from . import contact

# add contact page route                                                                                                                                                             
@contact.route('/contact')
def contactpage():
    form = ContactForm()

    # check form
    if request.method == 'POST':    
        # if valid tell user and redirect to home page 
        flash('Message Sent! Thank you for getting in touch.')
       # return redirect(url_for('contact'))
    return render_template('contact/contact.html', form=form, title='Contact Us')
