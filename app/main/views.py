from . import main
from flask import Flask, render_template
from flask_login import login_required

@main.route('/')
def index():

    title = 'Free Space'
    return render_template('index.html', title = title)



