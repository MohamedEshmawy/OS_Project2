import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class list_element(Gtk.Box):
	def __init__(self, label, delBtnLabel = "X", spacing=6):
		Gtk.Box.__init__(self)

		self.label = Gtk.Label(label)
		self.pack_start(self.label, True, True, 0)

		self.delBtn = Gtk.Button(label=str(delBtnLabel))
		self.pack_start(self.delBtn, True, True, 0)
		