import datetime
import json
from flask import Flask, redirect, render_template, request
import requests


app = Flask(__name__)


TASKS_FILE = "./config.json"


def getConfug():
    with open(TASKS_FILE, "r") as infile:
        return json.load(infile)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', config=getConfug())