from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearping_MUMDA313456"


@app.route("/")
@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greeter():
    name = str(request.form["name_input"])
    if name.rstrip() != "":
        flash("Hi " + name.capitalize() + ", great to see you!")
    else:
        flash("Hi Nobody, What's your name, again?")
    return render_template("index.html")
