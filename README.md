# lyric-model
CS 2803 Project

# About
This project uses the Genius API to search the lyrics of a song, and then feed that to a classifier that attempts to classify it by genre.
It is running on a python based Flask server, and uses a Bootstrap front end.
The user can type a song name into the search bar, at which time the server will send that song name to Genius,
and when the lyrics are returned, it feeds that string into the classifier using sklearn, and then displays the result.
The classifier was built using sklearn and can be seen in the Jupyter folder of this project.
To train it we scraped the Billboard website for the top 100 for each genre, and then fed the top 50 songs from each 
into the Genius API to get their lyrics. We then converted all of the lyrics of each genres into arrays of strings, 
mapped to a label which represents the genre. We then tried several classification methods but random forest had the 
highest accuracy, so we stuck with that. Again, all of the code for this portion can be seen in the Jupyter folder.
A running version can be seen on AWS C9 upon request (otherwise the server won't be running).

# Installation
Create a virtual environment for python3.6: `virtualenv vpy36`

Activate your virtualenv: `source vpy36/bin/activate`

Ensure python is version 3.6: `python --version`

Install all the requirements: `pip install -r requirements.txt`

Run the application: `python run.py`

Open your browser to `0.0.0.0:8080` to see the running application.

# Screenshots

![alt text](https://github.com/sidharth-potdar/lyric-model/blob/master/screenshots/home_page.png "Home Page")

![alt text](https://github.com/sidharth-potdar/lyric-model/blob/master/screenshots/gp_search.png "Search for God's Plan by Drake")

![alt text](https://github.com/sidharth-potdar/lyric-model/blob/master/screenshots/gp_result.png "Genre result for God's Plan")

![alt text](https://github.com/sidharth-potdar/lyric-model/blob/master/screenshots/ftb_search.png "Search for Fade to Black by Metallica")

![alt text](https://github.com/sidharth-potdar/lyric-model/blob/master/screenshots/ftb_result.png "Genre result for Fade to Black")