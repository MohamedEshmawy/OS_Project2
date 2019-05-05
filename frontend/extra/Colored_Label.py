#!/usr/bin/python3
import os
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
 
class Colored_Label(Gtk.Label):
	def __init__(self, label, color):
		Gtk.Label.__init__(self, label)
		self.color = Gdk.color_parse(color)
		rgba = Gdk.RGBA.from_color(self.color)
		self.override_background_color(0,rgba)
		self.connect('activate-link', self.click)

	def click(self, widget):
		self.override_background_color(0,Gdk.RGBA.from_color('red'))