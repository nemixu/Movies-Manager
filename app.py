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
app.secret_key = "super secret key"


mongo = PyMongo(app)

# Collections

users_collection = mongo.db.users
user_favorites = mongo.db.favorites


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

# Register an account

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already signed in!')
        return redirect(url_for('home'))
    if request.method == 'POST':
        form = request.form.to_dict()
        # checking passwords match
        if form['register_password'] == form['repeated_password']:
            user = users_collection.find_one({"username": form['username']})
            if user:
                flash(f"{form['username']} already exists!")
                return redirect(url_for('register'))
            else:
                # hashing password 
                hash_password = generate_password_hash(form['register_password'])
                users_collection.insert_one(
                    {
                        'username': form['username'],
                        'email' : form['email'],
                        'password': hash_password
                    }
                )
                # Checking to see if users details have been saved
                registered_user = users_collection.find_one({"username": form['username']})
                if registered_user:
                    session['user'] = registered_user['username']
                    flash("Your account has been created!")
                    return redirect(url_for('profile', user=registered_user['username']))
                else:
                    flash("There was an issue registering your account")
                    return redirect(url_for('register'))
        else:
            flash('Sorry your passwords do not match')
            return redirect(url_for('register'))
    return render_template('register.html') 

@app.route('/profile/<user>')
def profile(user): 
	# Check if user is logged in
	if 'user' in session:
		# If so get the user and pass him to template for now
		find_user = users_collection.find_one({"username": user})
		return render_template('profile.html', user=find_user, favorites_1=mongo.db.favorites.find())
	else:
		flash("You must be logged in!")
		return redirect(url_for('home'))


@app.route('/login', methods=['GET'])
def login():
    if 'user' in session:
        find_user = users_collection.find_one({"username": session['user']})
        if find_user:
            flash('You are already logged in!')
            return redirect(url_for('profile', user=find_user['username']))
    else:
        return render_template('login.html')



@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
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
    except KeyError:
        # will add code here to handle empty searches or searches that are not specific 
        return render_template('search.html')


@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    favorites=mongo.db.favorites
    favorites.insert_one(request.form.to_dict())
    return redirect(url_for('search'))
                    
@app.route('/favourites')
def favorites():
    return render_template('favourites.html', 
                           favorites=mongo.db.favorites.find())    


@app.route('/delete_favorites/<favorites_id>')
def delete_favorites(favorites_id):
    mongo.db.favorites.delete_one({'_id': ObjectId(favorites_id)})
    return redirect(url_for('favorites'))    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port= os.environ.get('PORT'),
            debug=True)


