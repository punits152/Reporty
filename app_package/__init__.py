from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"]= 'e44b0de08e7f665e2b19873e'

from app_package import routes