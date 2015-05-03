import os, Tkinter, Tkconstants, tkFileDialog

class Project():
    """ This class allows users to create a folder structure for their project. """
    
    PROGRAMS = ['After Effects', 'Audition', 'Illustrator', 'Photoshop', 'Premiere', 'Resolve']
    
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

        os.mkdir(self.directory + "/Final")
        os.mkdir(self.directory + "/Media")

    def create_folders(self, programs):
        self.programs = programs
        
        if 'After Effects' or 'Premiere' in self.programs:
            os.mkdir(self.directory + "/Media/Video")
        if 'After Effects' or 'Audition' or 'Premiere' in self.programs:
            os.mkdir(self.directory + "/Media/Audio")
        if 'Illustrator' or 'Photoshop':
            os.mkdir(self.directory + "/Media/Graphics")
        if 'After Effects' in self.programs:
            os.mkdir(self.directory + "/After_Effects")
        if 'Audition' in self.programs:
            os.mkdir(self.directory + "/Audition")
        if 'Premiere' in self.programs:
            os.mkdir(self.directory + "/Premiere")
        if 'Resolve' in self.programs:
            os.mkdir(self.directory + "/Media/Resolve")