# Programming Foundations in Python Final Project

For my Final Project, I will be creating a script that can encode movie files
based on user inputted settings to help automate the sometimes manual process
of needing to re-encode a movie for the web.

It will utilize the MoviePy project (and therefore ffmpeg) to transcode the
movies. This is a industry used toolset for high quality encoding.

The goal is for the user to run the script, be prompted with several questions
of what they need the encode to look like, and the script will create the file
for them.

## Project Design

The project will break down into two files: export_settings.py and export.py

**export_settings.py** will house the Class for the export object that will set
the file to be transcoded, the codec, bitrate, filename, etc. It will also
import the MoviePy library.

**export.py** will house the script that prompts the user for the settings they
want and call the object to do so. This will be the file that users will run.
