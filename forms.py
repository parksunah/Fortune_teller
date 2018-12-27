from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Please enter your name"})
    submit = SubmitField('See your fortune!')

class PhoneNumberForm(FlaskForm):
    friendname = StringField('Friend Name', validators=[DataRequired()], render_kw={"placeholder": "What's your friend's name?"})
    phone_number = StringField('Phone Number', validators=[DataRequired()], 
                                               render_kw={"placeholder": "What's your friend's phone number?"})
    submit = SubmitField('Send')