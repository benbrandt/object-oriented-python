import os, Tkinter, Tkconstants, tkFileDialog

class Project(Tkinter.frame):
    """ This class allows users to create a folder structure for their project. """

    VALID_PROGRAMS = ['After Effects', 'Audition', 'Illustrator', 'Photoshop', 'Premiere', 'Resolve']

    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        Tkinter.Button(self, text='askopenfile', command=self.askopenfile).pack(**button_opt)
        Tkinter.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt)
        Tkinter.Button(self, text='asksaveasfile', command=self.asksaveasfile).pack(**button_opt)
        Tkinter.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)
        Tkinter.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'

    def new_project(self, directory, project_name):
        self.directory = directory
        self.project_name = project_name

        self.project_dir = self.directory + "/" + self.project_name

        os.mkdir(self.project_dir)

    def select_programs(self, programs):
        self.programs = programs
