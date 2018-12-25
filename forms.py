from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('See your fortune!')

class PhoneNumberForm(FlaskForm):
    friendname = StringField('Friend Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()], 
                                               render_kw={"placeholder": "[country code][phone number including area code]"})
    submit = SubmitField('Share with friend!')