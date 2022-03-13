from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
import json
import os

# %%
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return os.popen('who').read().replace('\n', '<br/>')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  #HOME
        port=5000,
        debug=True,
        #        threaded=True
    )
