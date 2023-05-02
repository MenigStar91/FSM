# FSM
This project involves the development of a web application for hardware design analysis using Django . The purpose of the application is to provide users a platform for analyzing and evaluating different aspects of hardware designs for finite state machines into the main output file.We built this application using Django, as it being the most scalable and flexible application using python language.

# Setup 
Setting up the virtual environment for Django for backend
Installing the necessary libraries 
* pip install -r requirements.txt

Make migrations to update and previous state changes 
* python manage.py makemigrations

Run server at localhost 
* Python manage.py runserver
# Implementation of Backend code
* **Uploading**: This part is for uploading the code files into the server for storage . In this part we added file restriction to allow only uploading of .cpp and .v files . If any user try to add any other file then it will not get uploaded into the server
* **Code Refactoring**: To set proper paths for storage and uploading of the files.
* **Running the code**: This part is for running the .cpp code to generate a.exe file for output file generation 
* **Downloading** : This part is to enable downloading of the output generated files on clicking the link by the user on the desktop.
* **Deletion of files**: this part is to delete all the files being uploaded (.cpp and .v file) from the server so that server can use it for some other .cpp file and some other input .v file.

# Running 
python manage.py runserver 

