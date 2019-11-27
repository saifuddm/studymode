# Studymode
Automation script for when to enter study mode


# Things to work on:

* Open up document
* have it close ~~all links and~~ files
* have property when saving to mongo about tabnumber


# Things Added:
* Base script to open up all links in a browser
* Get current state of browser and have it export
* Set up mongoDB
* Load State for browser
* Added Simple UI
* Added parameters.yaml file containg mongoDB connections
* have classes for each course
* Send export state to mongoDB
* mongoDB extract and load 


# Imporve Features (ToDo):
* Disconnet the the app from the database by having it call node.js server and send it json data.
* Use of firebase to do authentication for user/pass for avenue

# BUGS
* MongoLoad will open an extra new tab
* MongoLoad doesn not load into correct order