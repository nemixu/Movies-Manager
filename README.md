# Movies Manager

Thank you for visiting my project.
This project was created as part of the CodeInstitute Full Stack Web Development Course,
This Project is for educational purposes only and is used to demonstrate the technologies learned in the course.

## Contents:

* UX 
    * Project Goals
    * Target Audience
    * Site Owner Goals
    * User Requirements and Expectations
    * Design Choices
        * Fonts
        * Icons
        * Colours 
        * Styling 
        * Images
        * Backgrounds
* WireFrames
* Features
    * Features that have been developed
    * Features that will be implimented in future deployments
* Technologies Used
* Testing
* Bugs
* Deployment
* Credits  

## UX (User Experience)
### Project Goals
The goal of this project is to create a web application that a user can interact with and search for their favorite movies. The users who access the website will be able to create a favorites list from movies they search delete a favourite they have added, and update the title and year of the movie.
This application contains the key CRUD requirement functionality and utilises a data handling document based database, MongoDB.

#### User Goals:

* To search movies I like, add to a favourites list
* Create an account where I can build up a favorites list to keep track of movies I like
* Visit a visually eppealing website
* Be able to consume information on my mobile device, desktop or tablet without any issues.
* Delete a movie from a list
* Edit a movie

#### User Stories:

* As a user I wish to create an account on the application
* As a user I wish to be able to search movies by name
* As a user I wish to add movies to a favorites list
* As a user I wish to be able to remove items from the above list whenever I want
* As a user I wish to be able to use this site on any device
* As a user I wish to edit a movie in my favourites


## User Requirements and Expectations:
##### Requirements:

* Interact with a visually appealing website
* Navigate the website with ease with fast loading times
* Find the movie I am looking with it showing a cover image of the movie
* Information to be easy to digest for the user

##### Expectations:

* The site protects the users information
* The user can interact with the elements on the page 
* The web application is usable on mutliple devices
* The website loads with sufficient speed
* The users are able to easily access their favorites

## Design Choices:

The website will use light and neutral colours to have a warm an inviting theme for a user for a friendly vibe to ensure the user would return again. Also it should reflect to help the user digest the information on the site easily.

#### Fonts: 

The font chosen for this project was <a href="https://fonts.google.com/specimen/Source+Sans+Pro">Source Sans Pro</a> as it was a sleek and clean font that made the information on the page pop and easy to read for the user.


#### Icons:

Icons used for this website were sourced from <a href="https://fontawesome.com/">Font Awesome</a> as it was easy to locate and preview the icons needed for best user experience for those interacting with the site.


#### Colours:

* ![#f4f4f4] - Background Colour
* ![#b3001b] - Button, Nav, Divider Colour
* ![#262626] - 
* ![#255c99] -
* ![#329f5B] -

#### Styling: 

*
*
*

#### Wireframes:

Wireframes for this projected were created using Balsamiq mockups.
Each wireframe was created using mobile first and each sketchup was done prior to the building of the site to ensure fast workflow.
Having done this provided me with drawings to work with whilst in the production phase and ensured I followed the exact steps and in return cut my production time in half.

#### Database planning:

As this was the first time working with databases and schemas I was unsure how to handle or tackle a project like this. My original plan for the database was to have a collection of Users: inside this document I would have username , email, password(hashed), and a unique id. After this I had a Favourites collection:  that had a list of favouirtes added by the user, which held title, year, poster, and imdbid code. After using this schema I found it to be problematic that If I added a user they would see all favouirtes as I did not declare a relationship between them.
I made a change to the schema and then added an array inside of the Users document that would show the users favourites only which was fine and worked well for the purpose.
An issue I then had was the relationship was still not valid as it was possible to duplicate the same movie favourite over and over instead of just calling the data already if it was once added to the database.

The Schema I final chose for this project was, a users relationship with many movies. The user collection and a favourites collection. Inside the user collection they would have a favourite Array that would house the favourites ID from the favourites collection.

favourites Collection:
Example

```json
{
  "_id": {
    "$oid": "5eea4926fbe2a5a0d4378163"
  },
  "title": "Batman Returns",
  "year": "1992",
  "imdbid": "tt0103776",
  "poster": "https://m.media-amazon.com/images/M/MV5BOGZmYzVkMmItM2NiOS00MDI3LWI4ZWQtMTg0YWZkODRkMmViXkEyXkFqcGdeQXVyODY0NzcxNw@@._V1_SX300.jpg"
}
```

users Collection:
Example
```json
{
  "_id": {
    "$oid": "5ee88da57289940080b3b142"
  },
  "username": "test",
  "email": "email@email.com",
  "password": "hashed Password goes here",
  "favourites": [
    {
      "$oid": "5eea4926fbe2a5a0d4378163"
    }
  ]
}

```

#### Background:

*
*
*

## Features:

* 
*
*
*
*

## Technologies Used:

### Languages:

* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.python.org/">Python</a>

### Tools & Libraries:

* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>
* <a href="https://www.mongodb.com/cloud/atlas">MongoDB Atlas</a>
* <a href="https://pymongo.readthedocs.io/en/stable/">PyMongo</a>
* <a href="https://flask.palletsprojects.com/en/1.0.x/">Flask</a>
* <a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a>


## Testing:

This section will be updated with testing done on this project.

#### Testing Planning:
This section will have the plans for testing this application

#### Defensive Testing:

This section will be updated with testing done on this project.

#### Testing Stories:
*
*
*
*

### Testing Outcome:

This project will not need alot of testing due to the scope of the application.



#### Bugs During Development:

To be regularly updated:

Had issues with login button on the login page, where the placeholder text on the button was off centrered on small screens, this was resolved with inline-size: min-content, this was tested through chrome dev tools and adjusting element styles to suit.

Had issues with landing image on the home page, I set the background image to absolute, any new items added for e.g (new container, row, cols) would position offset due to the absolute, removing this then resorted in the natural flow of the html items.

Issues with the search data that was displayhed from div's and h3's it would not post to DB correctly, added hidden text areas and it sent correctly, next issue was because each div was part of a for loop it would only post the first div field input even if we clicked the last input.

For loop on favourites page where I was using the incorrect variable name and it was not pulling the correct information.

Had issue with the profile variable, I had called a global variable and re-used the global name on a local variable and it was giving errors, changing the variable name resolved this.

One of the most difficult bugs / issues I had during the development of this application was with the favourites section, adding and removing a favourite. I was comparing a string vs a Object id, and when I was printing the data I was receiving like this.
{"$oid": "5ee88da57289940080b3b142"} but i needed just the "5ee88da57289940080b3b142" string value to compare, I was getting errors such as Object of type ObjectId is not JSON serializable, after resolving the issue and researching further a better solution would have been to add some form of json interp or bson interp, however wrapping the query in str() resolved the issues I was having.

I changed how the add to favourites worked and the favourites section, upon changing the queries i ran into errors like this, "<pymongo.cursor.Cursor object at 0x04694700>" and this was because I was passing into the database a string but was requesting and object id. when the object id was passed correctly into the favourites and called correctly the issue was resolved.

#### Known Bugs:

Known bugs will be highlighted here.

## Deployment:

This application was developed on Visual Studio Code, using git and GitHub to host the repository.

### Cloing the application from GitHub:

<strong>Ensure</strong> you have the following installed:
* PIP
* Python 3
* Git

<strong>Make sure you have an account at <a href="https://www.mongodb.com/">MongoDB</a> in order to construct the database.</strong>

<em>WARNING: You may need to follow a different guide based on the OS you are using, read more <a href="https://python.readthedocs.io/en/latest/library/venv.html">here.</a></em>

* 1: <strong>Clone</strong> the Movies Manager repository by either downloading from <a href="https://github.com/nemixu/movies-manager"> here</a>, or if you have Git installed typing the following command into your terminal.
```bash
git clone https://github.com/nemixu/movies-manager
```
* 2: <strong>Navigate</strong> to this folder in your terminal for e.g below.
```bash
cd movies-manager
```
* 3: <strong>Enter</strong> the following command into your terminal.
```bash
python3 -m .venv venv
```
* 4: <strong>Initilaize</strong> the environment by using the following command.
```bash
.venv\bin\activate 
```
* 5: <strong>Install</strong> the relevant requirements & dependancies from the requirements.txt file.
```bash
pip3 -r requirements.txt
```
* 6: In your IDE now <strong>create</strong> a file where you can store your SECRET_KEY and your MONGO_URI, follow the schema structure located in data/schemas to properly setup the Mongo Collections.
<em>NOTE: I developed this website on Visual Studio Code and used open variables within the APP.py. Replace the keys below.</em>
```json
{
    "python.pythonPath": "env/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintArgs": ["--load-plugins=pylint_flask"],
    "files.autoSave": "onFocusChange",
    "files.useExperimentalFileWatcher": true,
    "terminal.integrated.env.osx": {
      "SECRET_KEY": "<your_secret_key>",
      "DEV": "1",
      "FLASK_DEBUG": "1",
      "MONGO_URI": "<your_mongo_uri>"
    }      
}
```
* 7: Run the application using 
```bash
flask run 
```
or 
```bash
Python3 app.py
```

### Deploying Movies-Manager to Heroku:

* 1: <strong>Create</strong> a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```
* 2: <strong>Create</strong> a Procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
*2.1: <strong>Dynos</strong>will also need to be scaled.
```bash
heroku ps:scale web=1
```
* 3: <strong>Push</strong> these newly created files to your repository.
* 4: <strong>Create</strong> a new app for this project on the Heroku Dashboard.
* 5: <strong>Select</strong> your <strong>deployment</strong> method by clicking on the <strong>deployment</strong> method button and select GitHub.
* 6: On the dashboard, <strong>set</strong> the following config variables:

**Key**|**Value**
:-----:|:-----:
IP|0.0.0.0
PORT|5000
MONGO\_URI|mongodb+srv://<username>:<password>@<cluster\_name>-qtxun.mongodb.net/<database\_name>?retryWrites=true&w=majority
SECRET\_KEY|"your\_secret\_key"
* 7: Click the deploy button on the Heroku dashboard.
* 8: The site has been deployed the Heroku.




## Closing Notes:

Any additional notes to go here

## Credits: 

Miroslav Svec - for the solution on user logins and auth via hashing passwords, this was used and highly modified to suit project needs.
Simen Daehlin - For suggesting project ideas, reviewing project and also providing readme examples"
* <a href="http://www.omdbapi.com/">Movie API used</a>
* <a href="https://unsplash.com/">Stock Images used</a>