'''
Gui for creating decision trees using the decisiontree module and running them
on some data using the treerunner module

@author: Peter
'''
from tkinter import RIGHT, Tk, ttk, Toplevel, BOTH, Text, END, NONE, N, S, E, W, Grid, font, Canvas, LEFT, Y, NW, CENTER
from tkinter.filedialog import askopenfilename
from pathlib import Path
from treebuilder.treebuilder import buildTree, deleteTree
from treerunner.treerunner import runTree
from tkinter.constants import HORIZONTAL, DISABLED
import threading
import os

class Feedback:
    '''
    The feedback loop object for the ui
    '''
    
    def __init__(self, master):
        '''
        Sets up main ui window
        
        Arguments:
            master - The root tkinter object
        '''

        self.master = master
        self.help_window = None
        
        labelframeFont = font.Font(size = 11)
        labelFont = font.Font(size = 10)
        
        self.frame_builder = ttk.LabelFrame(master, height = 160, width = 720, labelwidget = ttk.Label(master, text = "Tree Builder", font = labelframeFont))
        self.frame_builder.pack()

        ttk.Label(self.frame_builder, text = "Questions:", font = labelFont).place(x = 25, y = 15)
        self.combobox_questionsfile = ttk.Combobox(self.frame_builder, values = self.getFiles("questions"), width = 30)
        self.combobox_questionsfile.place(x = 25, y = 40)
        ttk.Button(self.frame_builder, text = "Browse", command = lambda: self.browse(self.combobox_questionsfile)).place(x = 230, y = 38)

        ttk.Label(self.frame_builder, text = "Training Data:", font = labelFont).place(x = 325, y = 15)
        self.combobox_trainingfile = ttk.Combobox(self.frame_builder, values = self.getFiles("trainingdata"), width = 30)
        self.combobox_trainingfile.place(x = 325, y = 40)
        ttk.Button(self.frame_builder, text = "Browse", command = lambda: self.browse(self.combobox_trainingfile)).place(x = 530, y = 38)

        ttk.Label(self.frame_builder, text = "Tolerance:", font = labelFont).place(x = 625, y = 15)
        self.entry_tolerance = ttk.Entry(self.frame_builder, width = 10, justify = RIGHT)
        self.entry_tolerance.place(x = 625, y = 40)
        self.entry_tolerance.insert(0, "0.01")

        ttk.Label(self.frame_builder, text = "Tree Name:", font = labelFont).place(x = 25, y = 90)
        self.entry_treename = ttk.Entry(self.frame_builder, width = 24)
        self.entry_treename.place(x = 105, y = 90)
        ttk.Button(self.frame_builder, text = "Build", command = self.build).place(x = 262, y = 88)

        ttk.Label(self.frame_builder, text = "Print Tree", font = labelFont).place(x = 350, y = 90)
        self.check_printtree = ttk.Checkbutton(self.frame_builder, takefocus=False)
        self.check_printtree.place(x = 415, y = 90)
        self.check_printtree.invoke()

        self.frame_runner = ttk.LabelFrame(master, height = 160, width = 720, labelwidget = ttk.Label(master, text = "Tree Runner", font = labelframeFont))
        self.frame_runner.pack()
        
        ttk.Label(self.frame_runner, text = "Tree:", font = labelFont).place(x = 21, y = 15)
        self.combobox_treefile = ttk.Combobox(self.frame_runner, values = self.getFiles("trees"), width = 30)
        self.combobox_treefile.place(x = 25, y = 40)
        ttk.Button(self.frame_runner, text = "Delete", command = lambda: self.deleteCheck(self.combobox_treefile.get())).place(x = 230, y = 38)

        ttk.Label(self.frame_runner, text = "Data:", font = labelFont).place(x = 325, y = 15)
        self.combobox_datafile = ttk.Combobox(self.frame_runner, values = self.getFiles("data"), width = 30)
        self.combobox_datafile.place(x = 325, y = 40)
        ttk.Button(self.frame_runner, text = "Browse", command = lambda: self.browse(self.combobox_datafile)).place(x = 530, y = 38)

        ttk.Label(self.frame_runner, text = "Output Type:", font = labelFont).place(x = 25, y = 90)
        self.combobox_outputtype = ttk.Combobox(self.frame_runner, values = ["Output Only", "Full", "Print Tree"],  state = "readonly")
        self.combobox_outputtype.place(x = 115, y = 90)
        ttk.Button(self.frame_runner, text = "Run", command = lambda: self.run()).place(x = 265, y = 88)
        ttk.Label(self.frame_runner, text = "Print Results", font = labelFont).place(x = 353, y = 90)
        self.check_printresults = ttk.Checkbutton(self.frame_runner, takefocus=False)
        self.check_printresults.place(x = 438, y = 90)
        self.check_printresults.invoke()

        ttk.Button(self.frame_runner, text = "Help", command = lambda: self.help()).place(x = 630, y = 100)

    def browse(self, combobox):
        '''
        Have user select file from file browser and put that file in the appropriate combobox
        
        Arguments:
            combobox - The combobox to put the file in
        '''
        
        filename = askopenfilename()
        combobox.set(filename)
    
    def getFiles(self, filetype):
        '''
        Get the appropriate files from the appropriate folder to populate the combobox dropdown menu
        
        Arguments:
            filetype - Specifies which folder to get files from
        '''
        files = []
        
        path = Path(os.getcwd() + "/" + filetype)
        for x in path.iterdir():
            try:
                if not x.is_dir():
                    files.append(str(x).split("\\")[-1])
            except:
                pass
            
        return files
    
    def showProgressWindow(self, show, text = ""):
        '''
        Toggle function for progress bar window
        
        Arguments:
            show - Boolean, whether to show or destroy the window
            text - The string for the window title
        '''
        if show:
            self.progressWindow = Toplevel(self.master, takefocus=True)
            self.progressWindow.title(text)
            self.progressWindow.geometry('260x40+200+200')
            self.progressWindow.resizable(False, False)
            self.progressBar = ttk.Progressbar(self.progressWindow, orient = HORIZONTAL, length = 240, mode = 'indeterminate')
            self.progressBar.place(relx=0.5, rely=0.5, anchor = CENTER)
            self.progressBar.start()
            self.progressWindow.grab_set()
        else:
            self.progressBar.stop()
            self.progressBar.destroy()
            self.progressWindow.destroy()
    
    def buildWorker(self):
        '''
        Worker thread function for building the decision tree
        '''
        
        self.tree = buildTree(self.entry_treename.get(), self.combobox_trainingfile.get(), self.combobox_questionsfile.get(), self.entry_tolerance.get(), bool(self.check_printtree.state()))
        
    def buildCheck(self):
        '''
        Periodically checks if worker thread function is still alive, once it 
        is no longer alive if destroys the thread, the progress window, and 
        shows the readable version of the tree if the tree return a string
        '''
        
        if self.buildThread.is_alive():
            self.master.after(1000, self.buildCheck)
            
        else:
            
            #Catch user closing progress window
            try:
                self.showProgressWindow(False)
                
                if isinstance(self.tree, int):
                    self.errorWindow(self.tree)
                    self.buildThread._delete()
                    del(self.buildThread)
                    return
            
                elif isinstance(self.tree, str):
                    
                    window = Toplevel(self.master, takefocus=True)
                    window.title("Tree: " + self.entry_treename.get())
                    window.geometry('740x620+850+100')
                    
                    Grid.rowconfigure(window, 0, weight = 1)
                    Grid.columnconfigure(window, 0, weight = 1)
                    
                    xscrollbar = ttk.Scrollbar(window, orient=HORIZONTAL)
                    xscrollbar.grid(row=1, column=0, sticky=N+S+E+W)
        
                    yscrollbar = ttk.Scrollbar(window)
                    yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)
            
                    text = Text(window, wrap=NONE, xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set)
                    text.grid(row=0, column=0, sticky=N+S+E+W)
            
                    xscrollbar.config(command=text.xview)
                    yscrollbar.config(command=text.yview)
                    
                    text.insert(END, self.tree)
                    text.config(state = DISABLED)
                
                self.buildThread._delete()
                del(self.buildThread)
                self.updateBoxes()
            except:
                self.buildThread._delete()
                del(self.buildThread)
            
    def build(self):
        '''
        Handles the tree building and progress bar windows via threading
        '''
        
        self.buildThread = threading.Thread(target = self.buildWorker)
        
        self.showProgressWindow(True, "Building Tree")
        self.master.update()
    
        self.buildThread.start()
        self.buildCheck()
    
    def runWorker(self):
        '''
        Worker thread function for running the decision tree on some data
        '''
        
        self.results = runTree(self.combobox_treefile.get(), self.combobox_datafile.get(), self.combobox_outputtype.get(), bool(self.check_printresults.state()))
    
    def runCheck(self):
        '''
        Periodically checks if worker thread function is still alive, once it 
        is no longer alive if destroys the thread, the progress window, and 
        shows the readable version of the output if run fucntion returns a 
        string
        '''
        
        if self.runThread.is_alive():
            self.master.after(1000, self.runCheck)
            
        else:
            #Catch user closing progress window
            try:
                self.showProgressWindow(False)
                
                if isinstance(self.results, int):
                    self.errorWindow(self.results)
                    self.runThread._delete()
                    del(self.runThread)
                    return
                
                elif isinstance(self.results, str):
                
                    window = Toplevel(self.master, takefocus=True)
                    window.title("Tree: " + self.entry_treename.get())
                    window.geometry('740x620+850+100')
                    
                    Grid.rowconfigure(window, 0, weight = 1)
                    Grid.columnconfigure(window, 0, weight = 1)
                    
                    xscrollbar = ttk.Scrollbar(window, orient=HORIZONTAL)
                    xscrollbar.grid(row=1, column=0, sticky=N+S+E+W)
        
                    yscrollbar = ttk.Scrollbar(window)
                    yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)
            
                    text = Text(window, wrap=NONE, xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set)
                    text.grid(row=0, column=0, sticky=N+S+E+W)
            
                    xscrollbar.config(command=text.xview)
                    yscrollbar.config(command=text.yview)
                    
                    text.insert(END, self.results)
                    text.config(state = DISABLED)
                    
                    self.runThread._delete()
                    del(self.runThread)
            except:
                self.runThread._delete()
                del(self.runThread)
                
                
    def run(self):
        '''
        Handles the tree running and progress bar windows via threading
        '''
        
        self.runThread = threading.Thread(target = self.runWorker)
        
        self.showProgressWindow(True, "Running Tree")
        self.master.update()
    
        self.runThread.start()
        self.runCheck()
        
    
    def updateBoxes(self):
        '''
        Updates the comboboxes, for use when a new file is added to their
        corresponding folders
        '''
        
        self.combobox_trainingfile["values"] = self.getFiles("trainingdata")
        self.combobox_questionsfile["values"] = self.getFiles("questions")
        self.combobox_datafile["values"] = self.getFiles("data")
        self.combobox_treefile["values"] = self.getFiles("trees")
        
    def deleteCheck(self, tree):
        '''
        Confirmation window for deleting a tree, passes the tree along to the
        delete function if confirmed
        
        Arguments:
            tree - The name of the tree to delete
        '''
        if tree == "":
            return
        elif not tree in self.combobox_treefile["values"]:
            return
        
        window = Toplevel(self.master, takefocus=True)
        window.title("Confirm")
        window.resizable(False, False)
        ttk.Label(window, text = "Are you sure you want to delete " + tree.split("/")[0] + "?", padding = 20).pack(fill = BOTH, expand = True)
        ttk.Button(window, text = "Yes", command = lambda: self.delete(tree, window)).pack()
        ttk.Button(window, text = "No", command = lambda: self.closeWindow(window)).pack()
        window.grab_set()
    
    def closeWindow(self, window):
        '''
        Closes/destroys the given window
        
        Arguments:
            window - The window to destroy
        '''
        
        window.destroy()

    def delete(self, tree, window):
        '''
        Deletes the given tree and destroys the given window
        
        Arguments:
            tree - The tree to delete
            window - The window to destroy
        '''
        code = deleteTree(tree)
        
        if isinstance(code, int):
            self.errorWindow(code)
            return
        
        self.updateBoxes()
        self.combobox_treefile.set("")
        window.resizable(False, False)
        self.closeWindow(window)
        
    def help(self):
        '''
        Opens up a help window that explains each element of the ui and how to
        use the program in general
        '''
        
        if self.help_window != None:
            return
        
        self.help_window = Toplevel(self.master, takefocus=True)
        self.help_window.title("Help")
        self.help_window.geometry('720x800+850+100')
        self.help_window.resizable(False, False)
        self.help_window.protocol("WM_DELETE_WINDOW", self.closeHelpWindow)
        
        Grid.columnconfigure(self.help_window, 0, weight = 1)
        yscrollbar = ttk.Scrollbar(self.help_window)
        canvas = Canvas(self.help_window, yscrollcommand = yscrollbar.set, width = 700, scrollregion = (0, 0, 0, 1300))
        
        canvas.pack(side = LEFT, fill = BOTH)
        yscrollbar.config(command = canvas.yview)
        yscrollbar.pack(side = RIGHT, fill = Y)
        
        font1 = font.Font(family = "Ariel", size = 14, weight = "bold")
        font2 = font.Font(family = "Ariel", size = 12, weight = "bold")
        font3 = font.Font(family = "Ariel", size = 11)
        font4 = font.Font(family = "Ariel", size = 11, weight = "bold")
        
        canvas.create_text(5, 5, text = "Tree Builder:", font = font1, anchor = NW, width = 680)
        canvas.create_text(15, 35, text = "This will build a decision tree from the given questions and training data files.",
                           font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 65, text = "Questions:", font = font2, anchor = NW)
        canvas.create_text(15, 95, text = "These are the questions the tree will be built with. " +
                           "This should be a python file consisting of functions with a single argument that is an array of strings. " +
                           "There should be a special case where the argument is None and it should return an array of all possible outputs. " +
                           "Ideally these functions should split the data into the expected outcomes as best as possible. See the supplied files in the questions folder for examples. " +
                           "If using the browse button to select a file it will be added to the questions folder. Trees will use questions files from the questions folder, " +
                           "do not delete them if there is currently a tree that was built with them. Finally return values to these functions must be strings that do not contain " +
                           "the pound character (#). The pound character is reserved for parsing the tree later.", 
                          font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 250, text = "Training Data:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 280, text = "This is the training data the tree will be built with. " +
                          "This should be a plain text file with each line containing the data the questions should analyze followed by the given outcome. " +
                          "There should be one entry per line and questions should not attempt to split data using the given outcomes here as there will not be " +
                          "given outcomes in the data the tree will predict the outcome of. See the supplied files in the trainingdata folder for examples. " +
                          "If using the browse button to select a file it will be added to the trainingdata folder.",
                          font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 380, text = "Tolerance:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 410, text = "This is the tolerance for information gain the tree building algorithm will use to prune unnecessary questions from branches. " +
                           "This must be a number between 0 and 1, non-inclusive, and should ideally be scaled according to the number and complexity of the given questions. " +
                           "More information regarding the calculation of the question importance that is weighed against the given tolerance can be found in the documentation files.",
                           font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 510, text = "Tree Name:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 540, text = "This is the name of the tree file that will be produced. " +
                           "If a tree name is already in use it will overwrite the older tree without warning. The trees are stored in the trees folder.",
                           font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 590, text = "Print Tree:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 620, text =  "This option opens another window with a readable version of the tree once the tree has been built.",
                           font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 670, text = "Tree Runner:", font = font1, anchor = NW, width = 680)
        canvas.create_text(15, 700, text = "This will get the results from running the given tree on the given data files.",
                           font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 730, text = "Tree:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 760, text = "This is the tree that will be used to predict the outcomes of the data. Trees can be deleted using the delete button. " +
                          "This will only the delete the tree file and will not delete the questions or trainingdata files. " +
                          "Tree files should not be edited and one of the Print Tree options should be used to see an easily read version of the tree.",
                          font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 840, text = "Data:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 870, text = "This is the data file the tree will attempt to predict the outcomes of. " +
                          "This should be a plain text file with each line containing the data the questions should analyze. " +
                          "There should be one entry per line. See the supplied files in the data folder for examples. " +
                          "If using the browse button to select a file it will be added to the data folder.", 
                          font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 950, text = "Output Type:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 980, text = "This is how the Tree Runner will output the data. There are three options:", font = font3, anchor = NW, width = 680)
        canvas.create_text(15, 1010, text = "\tOutput Only:", font = font4, anchor = NW, width = 680)
        canvas.create_text(15, 1030, text = "\t\tThis will return only the predicted outcome and probability per line.", font = font3, anchor = NW, width = 680)
        canvas.create_text(15, 1050, text = "\tFull:", font = font4, anchor = NW, width = 680)
        canvas.create_text(15, 1070, text = "\t\tThis will return the line followed by the predicted outcome and probability per line.", font = font3, anchor = NW, width = 680)
        canvas.create_text(15, 1090, text = "\tPrint Tree:", font = font4, anchor = NW, width = 680)
        canvas.create_text(15, 1120, text = "\t\tThis will print the readable version of the tree like the Print Tree option when building\n\t\twithout having to rebuild the tree.", font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 1160, text = "Print Results:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 1190, text = "This option opens another window with the results of running the tree on the data in the format selected in the Output Type options. " +
                           "Results will be stored in the results folder according to that format as well.",
                           font = font3, anchor = NW, width = 680)
        
        canvas.create_text(5, 1240, text = "Help:", font = font2, anchor = NW, width = 680)
        canvas.create_text(15, 1270, text = "This button will open this window to provide information about using the Decision Tree Builder & Runner.",
                           font = font3, anchor = NW, width = 680)
        
    def closeHelpWindow(self):
        '''
        Handles closing the help window
        '''
        
        self.help_window.destroy()
        self.help_window = None
       
    def errorWindow(self, code):
        '''
        Creates an error window with a message based on the given error code
        
        Arguments:
            code - The code that specifies the error
        '''
        
        if code == 101:
            errorString = "The \"Tree Name\" field cannot be empty."
        elif code == 102:
            errorString = "The \"Training Data\" field cannot be empty."
        elif code == 103:
            errorString = "The \"Questions\" field cannot be empty."
        elif code == 104:
            errorString = "The \"Tolerance\" field cannot be empty."
        elif code == 105:
            errorString = "The \"Tree\" field cannot be empty."
        elif code == 106:
            errorString = "The \"Data\" field cannot be empty."
        elif code == 107:
            errorString = "The \"Output Type\" field cannot be empty."
            
        elif code == 201:
            errorString = "Could not find Training Data file."
        elif code == 202:
            errorString = "Could not find Questions file or there is an error in the file."
        elif code == 203:
            errorString = "Tolerance must be a number between 0 and 1."
        elif code == 204:
            errorString = "Failure to write Tree."
        elif code == 205:
            errorString = "Could not find Tree file."
        elif code == 206:
            errorString = "Could not find Questions file corresponding to given Tree file."
        elif code == 207:
            errorString = "Could not find Data file."
        elif code == 208:
            errorString = "Failure to write Results"
        elif code == 209:
            errorString = "Question return values cannot contain commas"
        elif code == 210:
            errorString = "Questions improperly formatted"
            
        elif code == 301:
            errorString = "Failure to build Tree."
        elif code == 302:
            errorString = "Failure to Parse Tree."
            
        window = Toplevel(self.master, takefocus=True)
        window.title("Error")
        window.resizable(False, False)
        ttk.Label(window, text = errorString, padding = 20).pack(fill = BOTH, expand = True)
        window.grab_set()
        
def runUI():
    root = Tk()
    root.title("Decision Tree Builder & Runner")
    root.resizable(False, False)
    root.geometry('740x330+50+100')
    feedback = Feedback(root)
    root.mainloop()