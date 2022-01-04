from logging import debug
from flask import Flask, render_template, request
import os
import re
from os import path
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_id=None
        email_id = str(request.form['email'])
        import login
        login.genrateSendOTP(email_id)
    return render_template('login.html',mail=email_id)

@app.route('/loginCheck', methods=['GET','POST'])
def loginCheck():
    if request.method == 'POST':
        myotp = str(request.form['otp'])
        import login
        if login.checkOTP(myotp):
            return render_template('home.html')
        else:
            return render_template('index.html',msg="Entered Wrong OTP")


if __name__ == '__main__':
    app.run(debug=True)