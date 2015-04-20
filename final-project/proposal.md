# Programming Foundations in Python Final Project

For my Final Project, I will be creating a script that can setup a series of
folders to create a directory template for new video projects. Based on the
workflow and pipeline of my current job.

It will utilize the Tkinter and os libraries to get user input and create the
folders.

The goal is for the user to run the script, be prompted with several questions
of what they need for their project, and the script will create the folders
for them.

## Project Design

The project will break down into two files: project_settings.py and
new_project.py

**project_settings.py** will house the Class for the folder creation object that
will create folders based on input. It will also import the os library.

**new_project.py** will house the script that prompts the user for the settings
they want and call the object to do so. Will import Tkinter.
