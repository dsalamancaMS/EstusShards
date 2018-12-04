from flask import Flask
from flask import render_template
import urllib.request

app = Flask(__name__)

@app.route("/")
def anor_londo():
    contents = urllib.request.urlopen("http://127.0.0.1:8082").read().decode("utf-8")
    return "Anor Londo => " + contents 