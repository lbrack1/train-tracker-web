# app/contact/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo 

class ContactForm(FlaskForm):
  """
  Form for user to contact
  """
  name = StringField("Name", validators=[DataRequired()])
  email = StringField("Email", validators=[DataRequired(), Email()])
  subject = StringField("Subject",validators=[DataRequired()])
  message = StringField("Message",validators=[DataRequired()])
  submit = SubmitField("Send")
