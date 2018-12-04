from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def izalith():
    return "Izalith on " + os.getenv("HOSTNAME")