import os, Tkinter, Tkconstants, tkFileDialog

class Project():
    """ This class allows users to create a folder structure for their project. """

    VALID_PROGRAMS = ['After Effects', 'Audition', 'Illustrator', 'Photoshop', 'Premiere', 'Resolve']

    def __init__(self):
        self = self

    def project_directory(self):
        """Returns a selected directoryname."""
        root = Tkinter.Tk()
        root.withdraw()
        dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        return dirname

    def new_project(self, directory):
        self.directory = directory

        os.mkdir(self.directory + "/new")

    def select_programs(self, programs):
        self.programs = programs
