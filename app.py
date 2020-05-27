import os 
from os import path
import time
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if path.exists("env.py"):
    import env

# Connection to Database
app = Flask(__name__)
app.config["MONGO_DBNAME"] = "movies_database"
app.config["MONGO_URI"] = "mongodb+srv://root:winter22@myfirstcluster-0xnxg.mongodb.net/movies_database?retryWrites=true&w=majority"


mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def test():
    return render_template("base.html")


# @app.route('/search-<search>')
# def search(search):
#     apikey = "3c0dea9f"
#     api = requests.get("http://www.omdbapi.com/?apikey={}&s={}".format(apikey, search))
#     data = api.json()

#     return data
#     print(data)

# search(search)   
            
@app.route('/login')
def login():
    return render_template('login.html') 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port= os.environ.get('PORT'),
            debug=True)


