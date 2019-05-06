import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Error_Dialog(Gtk.Dialog):
	def __init__(self,parent_window, error):
		Gtk.Dialog.__init__(self, "Error", parent_window)
		


		label_error = Gtk.Label(error)


		ok_btn = Gtk.Button('Ok')
		ok_btn.connect('clicked', self.on_ok_clicked)

				
		self.get_content_area().add(label_error)
		self.get_content_area().add(ok_btn)
		self.show_all()

	def on_ok_clicked(self, widget):
		self.destroy()