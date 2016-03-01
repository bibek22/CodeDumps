#!/usr/bin/env python

# time: Tue Nov 17 18:17:54 NPT 2015

from gi.repository import Gtk

class MainWindow(Gtk.Window):
    # class initialization
    def __init__(self):
        Gtk.Window.__init__(self, title="Audio converter")

        # stuffs
        inputFile = Gtk.Button(label="Choose a File")
        outputFolder = Gtk.Button(label="Output folder")
        targetFormat = Gtk.Entry()
        targetFormat.set_text("Target Format")

        self.fileSelected = Gtk.Entry()
        self.folderSelected = Gtk.Entry()
        
        start = Gtk.Button(label="Start!")
    



        # Main Grid/Frame of Gui.
        mainGrid = Gtk.Grid()
        self.add(mainGrid)

        #Adding stuff to the Frame.
        mainGrid.attach(self.fileSelected, 0, 0, 2, 1)
        mainGrid.attach(self.folderSelected, 0, 1, 2, 1)
        mainGrid.attach(inputFile, 2, 0, 1, 1)        
        mainGrid.attach(outputFolder, 2, 1, 1, 1)
        mainGrid.attach(targetFormat, 1, 2, 1, 1)
        mainGrid.attach(start, 0, 4, 1, 1)        

        # What do things do?
        inputFile.connect("clicked", self.getFile)
        outputFolder.connect("clicked", self.getFolder)
        self.fileSelected.set_text("get me some file")
        self.folderSelected.set_text("target folder")

        # Some variables you might need
        gotFile = ""
        gotFolder = ""
    
    # define getFile method
    def getFile(self, widget):

        dialog = Gtk.FileChooserDialog("Choose a file for conversion", self, Gtk.FileChooserAction.SELECT_FOLDER, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))

        dialog.set_default_size(600, 300)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.gotFile = dialog.get_filename()
            self.fileSelected.set_text(self.gotFile)
        elif response == Gtk.ResponseType.CANCEL:
            print("try again!")

        dialog.destroy()
            
        # define getFolder method
    def getFolder(self, widget):

        dialog = Gtk.FileChooserDialog("choose a target folder", self, Gtk.FileChooserAction.SELECT_FOLDER, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))

        dialog.set_default_size(600, 300)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.gotFolder = dialog.get_filename()
            self.folderSelected.set_text(self.gotFolder)
        elif response == Gtk.ResponseType.CANCEL:
            print("try again!")

        dialog.destroy()


Window = MainWindow()
Window.connect("delete-event", Gtk.main_quit)
Window.show_all()
Gtk.main()
