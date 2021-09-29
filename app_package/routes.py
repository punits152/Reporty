from flask.templating import render_template
from app_package import app
from app_package import forms

@app.route("/",methods=["POST","GET"])
def home_page():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login_page():
    form = forms.RegisterForm()
    return render_template("login_page.html",form=form)