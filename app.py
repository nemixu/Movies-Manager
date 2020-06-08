import os 
from os import path
import time
import requests
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
def home():
    return render_template("home.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        searchTerm = request.form['search-term']
        apikey = "3c0dea9f"
        api = requests.get("http://www.omdbapi.com/?apikey={}&s={}".format(apikey, searchTerm))
        data = api.json()
        print(data)
        returnResults = list()
        for movies in data['Search']:
            title = movies['Title']
            year = movies['Year']
            imdb = movies['imdbID']
            poster = movies['Poster']
            movieDetails = [title, year, imdb, poster]
            returnResults.append(movieDetails)
        print(returnResults)
        return render_template('search.html', returnResults=returnResults)
    else:
        return render_template('search.html')


@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    favorites=mongo.db.favorites
    favorites.insert_one(request.form.to_dict())
    return redirect(url_for('search'))
   
@app.route('/favorites')
def favorites():

    return render_template('favorites.html', 
                           favorites=mongo.db.favorites.find())
    








# @app.route('/remove_favorite/', methods=['POST'])
# def remove_favorite():
#     mongo.db.favorites.remove({'_id': ObjectId(task_id)})
#     return redirect(url_for('favorites')  
               








@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html') 


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html') 
 
 
 
  
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port= os.environ.get('PORT'),
            debug=True)


