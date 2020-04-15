# Packages
from flask import render_template, jsonify, request

# Methods
from flaskmail import app
from flaskmail.mail import send_gmail

# Creating Routes
# HTML ROUTES


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# JSONROUTES


@app.route('/json')
@app.route('/json/home', methods=['GET'])
def json_home():
    return jsonify({"Name": "Atharva"})


@app.route('/json')
@app.route('/json/sendemail', methods=['POST'])
def json_send_email():
    send_gmail(request.json['email'],
               request.json['subject'], request.json['body'])
    return jsonify({"Response": "Sent"})
