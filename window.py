import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class OSWindow2(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="OS PROJECT 2")

        self.set_border_width(10)



        self.connect('destroy', Gtk.main_quit)
        self.show_all()


    def run(self):
        Gtk.main()
