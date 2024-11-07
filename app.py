from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('home.html')
    
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

        





