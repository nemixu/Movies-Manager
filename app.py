import os
from os import path
import requests
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if path.exists('env.py'):
    import env

# Connection to Database
APP = Flask(__name__)
APP.config["MONGO_DBNAME"] = os.getenv('MONGODB_NAME')
APP.config["MONGO_URI"] = os.getenv('MONGO_URI')
APP.secret_key = os.getenv('SECRET_KEY')
mongo = PyMongo(APP)


# Collections
users_collection = mongo.db.users
favourites_collection = mongo.db.favourites


@APP.route('/')
@APP.route('/home')
def home():
    '''
    Home function, that holds the recent favourites to be displayed to users.
    '''
    return render_template("home.html", recents=favourites_collection.find())


# Register an account
@APP.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Checks user is not already logged in, register if they are not present in db
    '''
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
                hash_password = generate_password_hash(
                    form['register_password'])
                users_collection.insert_one(
                    {
                        'username': form['username'],
                        'email': form['email'],
                        'password': hash_password,
                        'favourites': []
                    }
                )
                # Checking to see if users details have been saved
                registered_user = users_collection.find_one({"username": form['username']})
                if registered_user:
                    session['user'] = str(registered_user['_id'])
                    flash("Your account has been created!")
                    return redirect(url_for('profile', user=registered_user['username']))
                else:
                    flash("There was an issue registering your account")
                    return redirect(url_for('register'))
        else:
            flash('Sorry your passwords do not match')
            return redirect(url_for('register'))
    return render_template('register.html')

# User profile
@APP.route('/profile/<user>')
def profile(user):
    '''
    find user profile and return logged in profile and return favourites
    '''
    if 'user' in session:
        find_user = users_collection.find_one({"_id": ObjectId(session["user"])}, {"_id": 1})
        user_session = find_user['_id']
        user_favs_ids = users_collection.find_one({"_id": ObjectId(session['user'])},
                                                  {"favourites": 1})
        user_favs = favourites_collection.find({"_id": {"$in": user_favs_ids["favourites"]}})
        user_account = users_collection.find_one({"_id": ObjectId(session['user'])},
                                                 {"username": 1})
        return render_template('profile.html',
                               user=user_session, user_favs=user_favs, user_account=user_account)
    flash("You must be logged in!")
    return redirect(url_for('home'))

# Login route
@APP.route('/login', methods=['GET'])
def login():
    '''
    Find user by username on form submission
    '''
    if 'user' in session:
        find_user = users_collection.find_one({"_id": ObjectId(session["user"])}, {"_id": 1})
        if find_user:
            flash('You are already logged in!')
            return redirect(url_for('profile', user=find_user['_id']))
    else:
        return render_template('login.html')

# Authenticate User form request
@APP.route('/auth', methods=['POST'])
def auth():
    '''
    Authenticate the user off their form input vs the users collection,
    and their password vs the hashed password
    '''
    form = request.form.to_dict()
    find_user = users_collection.find_one({"username": form['username']})
    # Check for user in database
    if find_user:
        # If passwords match (hashed / real password)
        if check_password_hash(find_user['password'], form['user_password']):
            # Log user in (add to session)
            session['user'] = str(find_user['_id'])
            # If the user is admin redirect him to admin area for future release
            if session['user'] == "admin":
                return redirect(url_for('admin'))
            else:
                flash("You were logged in!")
                return redirect(url_for('profile', user=find_user['_id']))
        else:
            flash("Wrong password or username!")
            return redirect(url_for('login'))
    else:
        flash("You must be registered!")
        return redirect(url_for('register'))


@APP.route('/logout')
def logout():
    '''
    Logout results in clearing the session and logging user out
    '''
    session.clear()
    flash('You have been logged out!')
    return redirect(url_for('home'))


@APP.route('/search', methods=['GET', 'POST'])
def search():
    '''
    On request, handles request from api,
    returns movies and is appended to movie_results
    '''
    try:
        if request.method == 'POST':
            search_term = request.form['search-term']
            apikey = "3c0dea9f"
            api = requests.get(
                "http://www.omdbapi.com/?apikey={}&s={}".format(apikey, search_term))
            data = api.json()
            movie_results = list()
            for movies in data['Search']:
                movie_results.append([movies['Title'], movies['Year'], movies['imdbID'], movies['Poster']])
            return render_template('search.html', movie_results=movie_results)
        else:
            return render_template('search.html')
    except KeyError:
        # will add code here to handle empty searches or searches that are not specific
        return render_template('search.html')


@APP.route('/add_favorite', methods=['POST'])
def add_favorite():
    '''
    Checks users favourites if does not exist,
    add favourite to users collection
    '''
    if 'user' in session:
        # Get all the oid from favourites using the imdbid
        existing_fav_id = list(favourites_collection.find({"imdbid": request.form.to_dict()["imdbid"]}, {"_id": 1}))
        fav_id_arr = []
        for fav in existing_fav_id:
            fav_id_arr.append(fav["_id"])
        # Compare the oids to the list of user favourite ids.
        user_fav_id = users_collection.count_documents({"_id": ObjectId(session["user"]), "favourites": {"$in": fav_id_arr}})
        if user_fav_id > 0:
            flash('Movie already added to your favourites!')
        else:
            # Save favourite to DB and store object ID into favourites of the currently logged in user
            new_fav_id = favourites_collection.insert_one(request.form.to_dict()).inserted_id
            users_collection.update_one({'_id': ObjectId(session['user'])}, {'$push': {'favourites': ObjectId(new_fav_id)}})
            flash('Movie added to your favourites!')
        return redirect(url_for('search'))
    else:
        flash('You must be logged in to add a favourite')
        return render_template('login.html')


@APP.route('/favourites')
def favorites():
    '''
    Get all the users favourites from the user that is logged in,
    get all the favourites where the _id is in the array of the users favourite ids
    '''
    user_favs_ids = users_collection.find_one({"_id": ObjectId(session['user'])}, {"favourites": 1})
     # Get all the favourites where the _id is in the array of the users favourite ids
    user_favs = favourites_collection.find({"_id": {"$in": user_favs_ids["favourites"]}})
    return render_template('favourites.html', user={"favourites": user_favs})


@APP.route('/delete_favorites/<favorites_id>')
def delete_favorites(favorites_id):
    '''
    Deleting a favourite from the users collection,
    removing the movies from favs array
    '''
    if 'user' in session:
        user_id = session['user']
        users_collection.update_one({'_id': ObjectId(user_id)}, {'$pull': {"favourites": ObjectId(favorites_id)}})
        # Delete the favourites document by favourite_id
        favourites_collection.remove({'_id': ObjectId(favorites_id)})
        flash('Movie removed from your list')
    else:
        flash('You must be logged in to remove this item')
    return redirect(url_for('favorites'))

@APP.route('/edit', methods=['POST'])
def edit():
    '''
    Edit a favourite from the users collection
    '''
    if 'user' in session:
        query = {'_id': ObjectId(request.form.get('_id'))}
        projection = {'title': request.form.get('title'), 'year': request.form.get('year')}
        # Edit the favourites document by favourite_id
        favourites_collection.update_one(query, {'$set': projection})
        flash('Movie details updated')
    else:
        flash('You must be logged in to remove this item')
    return redirect(url_for('profile', user=session['user']))



if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)