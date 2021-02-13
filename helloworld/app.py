from flask import Flask, render_template, redirect, abort, request, session, url_for


app = Flask(__name__)

# To be replaced with a randomly generated value
app.config["SECRET_KEY"] = "ToBeReplacedWithSomethingRandom"


# TODO: Maybe the home page should show some basic instruction how to use the app, if there is anything to explain.
@app.route("/")
def home():
    return render_template("hello.html", name="world")


#TODO: The parameter name will be replaced with a numerical ID refering to an object in the database.
@app.route("/hello-world/<name>")
def hello(name):
    # return f"<h1>Hello, {name}!</h1>"
    return render_template("hello.html", name=name)


# TODO: I would like to have make it easy to open the greeting page for some existing persons to get things started.
@app.route("/listpersons")
def listpersons():
    return render_template('not_implemented_yet.html')


@app.route("/admin")
def admin():
    return render_template('not_implemented_yet.html')


if __name__ == "__main__":
    app.run()
