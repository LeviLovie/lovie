import datetime
import json
from flask import Flask, redirect, render_template, request, send_from_directory
import requests

app = Flask(__name__)
# app.run(debug=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6000, debug=True)

PROJECTS_FILE = "./projects.json"
CONFIG_FILE = "./config.json"

def getConfug():
    with open(CONFIG_FILE, "r") as infile:
        return json.load(infile)

def getProjects():
    with open(PROJECTS_FILE, "r") as infile:
        return json.load(infile)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', config = getConfug(), projects = getProjects())

@app.route('/mainstyle', methods=['GET'])
def mainstyle():
    return send_from_directory('styles', 'mainstyle.css')

@app.route('/smallstyle', methods=['GET'])
def smallstyle():
    return send_from_directory('styles', 'smallstyle.css')

@app.route('/<section>', methods=['GET'])
def vindigio(section):
    return render_template('project.html', project = getProjects().get(section))

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)