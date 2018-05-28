from . import main
from flask import Flask, render_template

@main.route('/')
def index():

    title = 'Free Space'
    return render_template('index.html', title = title)



