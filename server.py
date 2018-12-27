from jinja2 import StrictUndefined
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import forms
import random
from twilio.rest import Client
import os

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def home():
    user_form = forms.NameForm()

    return render_template('home.html', form=user_form)

@app.route('/fortune', methods=['POST'])
def show_fortune():
  
    username = request.form['username']
    friend_form = forms.PhoneNumberForm()
  
    with open('fortune.txt') as f:
        lines = f.readlines()
  
    return render_template('fortune.html', username=username, form=friend_form, fortune_text = random.choice(lines))


@app.route('/fortune_delivery', methods=['POST'])
def fortune_delivery():
  
    username = request.form['username']
    friendname = request.form['friendname']
    phone_num = request.form['phone_number']

    with open('fortune.txt') as f:
        lines = f.readlines()

    random_fortune = "Hi," + friendname + \
                     "This is a today's fortune your friend -" + username + "- sent :" + \
                     random.choice(lines)

    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    client = Client(account_sid, auth_token)


    message = client.messages \
                    .create(
                         body=random_fortune,
                         from_='+15072600733',
                         to=phone_num
                     )

  
    return render_template('fortune_delivery.html', friendname=friendname, phone_num=phone_num, fortune_text = random_fortune)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')