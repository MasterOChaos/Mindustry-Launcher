#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys
import os.path


#UI file
UI_FILE = "mindustrylauncher.ui"


class GUI:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')


		window.show_all()

	def on_window_destroy(self, window):
		Gtk.main_quit()

def main():
	app = GUI()
	Gtk.main()
		
handlers = {
    "on_VERSION_editing_done": entry.get_text() = version,
    "on_LAUNCH_button_press_event": os.system("wget https://github.com/Anuken/Mindustry/releases/download/v" + version + "/Mindustry.jar")
}
builder.connect_signals(handlers)

if __name__ == "__main__":
	sys.exit(main())

