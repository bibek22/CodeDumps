#!/usr/bin/env python

from gi.repository import Gtk


# class DownlaodInstance(Gtk.List):
#     def __init__(self, parent, title, position, status, size, speed, timeleft):
#         self.title = title
#         self.position = position
#         self.status = status
#         self.size = size
#         self.speed = speed
#         self.timeleft = timeleft
#         self.parent = parent
#         Gtk.ListBox.__init__(self, str, int, bool, str, str, str)
#         self.append(self.title, self.position, self.status, self.size, self.size, self.speed, self.timeleft)
#         parent.add(self,)

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Youtube Downloader")
        self.set_border_width(10)
        self.set_default_size(530, 240)

        # variables first
        urllabel = "Get me the URL."
        llabel = "Save to"
        avlabel = "Audio/Video"
        calLabel = "Choose Quality"
        defloc = "~/music"
        pantalla = Gtk.Notebook()
        # pantalla.set_transittion_type(Gtk.StackTransitionType.
        #                              SLIDE_LEFT_TO_RIGHT)
        pantalla.set_border_width(5)

        self.add(pantalla)

        urlquery = Gtk.Label(urllabel, xalign=0)

        lquery = Gtk.Label(llabel, xalign=0)

        av = Gtk.Label(avlabel, xalign=0)
        # av.justification(Gtk.Justification.LEFT)

        calidad = Gtk.Label(calLabel)
        # calidad.justification(Gtk.Justification.LEFT)

        start = Gtk.Button("Go!")

        mainvertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        downloadpage = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        pantalla.append_page(mainvertical, Gtk.Label('Main Page'))
        pantalla.append_page(downloadpage, Gtk.Label("Progress"))

        urlbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        locbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        typebox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=40)
        calbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=40)
        # box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        urlentry = Gtk.Entry()
        locentry = Gtk.Entry()
        locentry.set_text(defloc)
        avswitch = Gtk.Switch()
        calistore = Gtk.ListStore(str)
        calidads = ["360p", "480p", "720p"]
        for each in calidads:
            calistore.append([each])

        calicombo = Gtk.ComboBox.new_with_model(calistore)

        mainvertical.pack_start(urlbox, True, True, 0)
        mainvertical.pack_start(locbox, True, True, 0)
        mainvertical.pack_start(typebox, True, True, 0)
        mainvertical.pack_start(calbox, True, True, 0)
        mainvertical.pack_start(start, True, True, 0)

        urlbox.pack_start(urlquery, True, True, 0)
        urlbox.pack_start(urlentry, True, True, 0)
        locbox.pack_start(lquery, True, True, 0)
        locbox.pack_start(locentry, True, True, 0)
        typebox.pack_start(av, True, True, 0)
        typebox.pack_end(avswitch, False, True, 10)
        calbox.pack_start(calidad, False, True, 0)
        calbox.pack_start(calicombo, True, True, 0)


window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
