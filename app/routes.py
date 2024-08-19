from flask import render_template, request, redirect, url_for
from app import app
from app.dataBase import get_availability

@app.route('/')
def index():
    month = request.args.get('month', 'next')
    availability = get_availability(month)
    return render_template('index.html', availability=availability)

@app.route('/confirm/<date>')
def confirm(date):
    # If more time is available, db logic and whatnot here
    return render_template('success.html', date=date)

@app.route('/success')
def success():
    date = request.args.get('date')
    return render_template('success.html', date=date)
