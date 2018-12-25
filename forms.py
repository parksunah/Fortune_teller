from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class NameForm(FlaskForm):
    username = StringField('Name')
    submit = SubmitField('See your fortune!')

class PhoneNumberForm(FlaskForm):
    friendname = StringField('Friend Name')
    phone_number = StringField('Phone Number')
    submit = SubmitField('Share with friend!')