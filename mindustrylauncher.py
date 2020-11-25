#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys
import os.path
import urllib.request

#UI file
UI_FILE = "mindustrylauncher.ui"


class GUI:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')
		playlat = self.builder.get_object('playlatest')
		play5 = self.builder.get_object('playv5')
		play4 = self.builder.get_object('playv4')
		uplat = self.builder.get_object('updatelatest')
		up5 = self.builder.get_object('updatev5')
		up4 = self.builder.get_object('updatev4')
		
		window.show_all()

	def on_window_destroy(self, window):
		Gtk.main_quit()
		sys.exit("Exited Sucessfully")
	
	def on_playlatest_clicked(self, playlat):
		userpath = os.path.expanduser('~')
		v6pathj = userpath + "/.cache/mindustrylauncher/v6/m.jar"
		os.system("java -jar " + v6pathj)
	def on_playv5_clicked(self, play5):
		userpath = os.path.expanduser('~')
		v5pathj = userpath + "/.cache/mindustrylauncher/v5/m.jar"
		os.system("java -jar " + v5pathj)
	def on_playv4_clicked(self, play4m):
		userpath = os.path.expanduser('~')
		v4pathj = userpath + "/.cache/mindustrylauncher/v4/m.jar"
		os.system("java -jar " + v4pathj)
	def on_updatelatest_clicked(self, uplat):
		userpath = os.path.expanduser('~')
		v6path = userpath + "/.cache/mindustrylauncher/v6"
		v6pathj = userpath + "/.cache/mindustrylauncher/v6/m.jar"
		urll = 'https://github.com/Anuken/Mindustry/releases/download/v117.1/Mindustry.jar'
		try:
			os.mkdir(v6path)
			urllib.request.urlretrieve(urll, v6pathj)
			print('Downloaded Latest')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
		except OSError as error:
			os.remove()
			urllib.request.urlretrieve(urll, v6pathj)
			print('Downloaded Latest')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
		except OSError as error:
			urllib.request.urlretrieve(urll, v6pathj)
			print('Downloaded Latest')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
	def on_updatev5_clicked(self, up5m):
		userpath = os.path.expanduser('~')
		v5path = userpath + "/.cache/mindustrylauncher/v5"
		v5pathj = userpath + "/.cache/mindustrylauncher/v5/m.jar"
		url5 = 'https://github.com/Anuken/Mindustry/releases/download/v104.6/Mindustry.jar'
		try:
			os.makedirs('cache/Mindustrylauncher/v5')
			urllib.request.urlretrieve(url5, v5pathj)
			print('Downloaded V5')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
		except OSError as error:
			os.remove('cache/Mindustrylauncher/v5/m.jar')
			urllib.request.urlretrieve(url5, v5pathj)
			print('Downloaded V5')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
		except OSError as error:
			urllib.request.urlretrieve(url5, v5pathj)
			print('Downloaded V5')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
	def on_updatev4_clicked(self, up4):
		url4 = 'https://github.com/Anuken/Mindustry/releases/download/v96/Mindustry.jar'
		userpath = os.path.expanduser('~')
		v4path = userpath + "/.cache/mindustrylauncher/v4"
		v4pathj = userpath + "/.cache/mindustrylauncher/v4/m.jar"
		try:
			os.makedirs(v4path)
			urllib.request.urlretrieve(url4, v4pathj)
			print('Downloaded V4')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
		except OSError as error:
			os.remove(v4pathj)
			urllib.request.urlretrieve(url4, v4pathj)
			print('Downloaded V4')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
		except OSError as error:
			urllib.request.urlretrieve(url4, v4pathj)
			print('Downloaded V4')
			downwin = self.builder.get_object('downwindow')
			downwin.show_all()
			
def main():
	app = GUI()
	Gtk.main()
		

if __name__ == "__main__":
	sys.exit(main())
