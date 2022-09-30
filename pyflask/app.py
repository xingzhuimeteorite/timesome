from xml.etree.ElementTree import PI
from flask import Flask
from objectpic import Pic
app = Flask(__name__)
@app.route("/shanshan")
def hello_world():
    return "timesome/front/index.html"


@app.route("/static/<dir>/<name>")
def return_pic(dir,name):
    pic = Pic(dir,name)
    return pic.get_img()
