from flask import Flask,render_template
from objectpic import Pic
app = Flask(__name__,template_folder='front',static_folder='front',static_url_path='')
@app.route("/shanshan")
def hello_world():
    return render_template("index.html")


@app.route("/static/<dir>/<name>")
def return_pic(dir,name):
    pic = Pic(dir,name)
    return pic.get_img()

app.run(host='0.0.0.0',port=5000)