import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from backend.data_containers.Memory import Memory
from backend.data_containers.Hole import Hole
from backend.data_containers.Process import Process
from backend.data_containers.Segment import Segment
from frontend.Views.Output_Dialog import Output_Dialog


class Test(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Test")
        self.set_border_width(10)

        memory = Memory()
        memory.size = 150

        P0 = Process(name = "P0")

        P0S0 = Segment(P0, "S0", 50)
        P0S0.start_address = 50

        P0S1 = Segment(P0, "S1", 25)
        P0S1.start_address = 125

        H0 = Hole(0, 50)
        H1 = Hole(100, 25)

        P0.add_segment(P0S0)
        P0.add_segment(P0S1)

        memory.add_process(P0)
        memory.add_hole(H0)
        memory.add_hole(H1)

        self.add(Output_Dialog(self, memory))
        
        self.connect('destroy', Gtk.main_quit)
        self.show_all()


    def run(self):
        Gtk.main()

window = Test()
window.run()