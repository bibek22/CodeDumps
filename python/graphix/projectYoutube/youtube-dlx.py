#!/usr/bin/python
import subprocess
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Youtube-dl GUI")
        self.set_border_width = 10


# Wanna create something? Create here.

        # Prompt for Url of video.
        getMeTheURL = Gtk.Label()
        getMeTheURL.set_text("Enter the URL:")

        # URL input field
        self.url = Gtk.Entry()
        self.url.set_text("Paste the URL")

        # Start download button
        download = Gtk.Button(label="Start!")
        download.connect("clicked", self.startDownload)

        # Folder chooser
        self.location = Gtk.Button(label="Choose folder")
        self.location.connect("clicked", self.filechooser)

        # Display for what's going on!
        self.show = Gtk.Label()
        self.show.set_text("No download process running at the moment.")

        # Main grid.
        grid = Gtk.Grid()
        self.add(grid)

# Put your things where you wanna put below.

        # Attaching to the main Grid.
        grid.attach(getMeTheURL, 0, 0, 1, 1)
        grid.attach(self.location, 1, 1, 2, 1)
        grid.attach(self.url, 0, 1, 1, 1)
        grid.attach(download, 3, 1, 1, 1)
        grid.attach(self.show, 0, 3, 3, 2)

        # default location
        self.folder = "/home/bibek/music/"

    def startDownload(self, widget):
        # self.url.get_text()
        arg = "https://www.youtube.com/watch?v=cKq0m3_aBoM"
        location = " -o '" + self.folder + "/%(title)s.%(ext)s'"
        program = "youtube-dl " + arg
        print([program, arg, "-o", location])
        # program, arg, "-o", location
        print("youtube-dl", arg, location)
        download_process = subprocess.Popen([program, location],
                                            shell=True, stdout=subprocess.PIPE)
        print(download_process.stdout.readline())

    def filechooser(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
                                       Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL,
                                        Gtk.ResponseType.CANCEL,
                                        "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(600, 300)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.folder = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
