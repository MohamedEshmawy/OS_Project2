import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from frontend.containers.Hole_list_element import Hole_list_element

class OSWindow2(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="OS PROJECT 2")

		self.set_border_width(10)

		self.listbox = Gtk.ListBox()


		self.element1 = Hole_list_element('blablablaaaabla', '1',  self.delete_hole)
		element2 = Hole_list_element('llalaaalalaaablaaaaaaaaa', '2', self.delete_hole)

		self.listbox.add(self.element1)
		self.listbox.add(element2)

		self.add(self.listbox)

		self.connect('destroy', Gtk.main_quit)
		self.show_all()


	def run(self):
		Gtk.main()

	def delete_hole(self, widget, *data):
		widget.label.set_text(data[0])
