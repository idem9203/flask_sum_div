from flask import Flask
app = Flask(__name__)

@app.route("/acerca")
def hello():
    return "acerca"

@app.route("/suma/<int:s1>/<int:s2>", methods=["GET"])
def suma(s1,s2):
    return str(s1+s2)

@app.route("/division/<int:d1>/<int:d2>", methods=["GET"])
def divide(d1,d2):
    return str(d1/d2)
