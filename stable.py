#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import wx, os, sys
import urllib.request
import os.path

class MAINAPP(wx.Frame):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.SetSize((220, 220))
		self.SetTitle("Mindustry Launcher")

		grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)

		label_1 = wx.StaticText(self, wx.ID_ANY, "LATEST")
		grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

		self.pvl = wx.Button(self, wx.ID_ANY, "PLAY")
		grid_sizer_1.Add(self.pvl, 0, wx.EXPAND, 0)

		self.uplat = wx.Button(self, wx.ID_ANY, "UPDATE")
		grid_sizer_1.Add(self.uplat, 0, wx.EXPAND, 0)

		label_2 = wx.StaticText(self, wx.ID_ANY, "V5")
		grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER, 0)

		self.pv5 = wx.Button(self, wx.ID_ANY, "PLAY")
		grid_sizer_1.Add(self.pv5, 0, wx.EXPAND, 0)

		self.upv5 = wx.Button(self, wx.ID_ANY, "UPDATE")
		grid_sizer_1.Add(self.upv5, 0, wx.EXPAND, 0)

		label_3 = wx.StaticText(self, wx.ID_ANY, "V4")
		grid_sizer_1.Add(label_3, 0, wx.ALIGN_CENTER, 0)

		self.pv4 = wx.Button(self, wx.ID_ANY, "PLAY")
		grid_sizer_1.Add(self.pv4, 0, wx.EXPAND, 0)

		self.upv4 = wx.Button(self, wx.ID_ANY, "UPDATE")
		grid_sizer_1.Add(self.upv4, 0, wx.EXPAND, 0)

		self.SetSizer(grid_sizer_1)

		self.Layout()

		self.Bind(wx.EVT_BUTTON, self.pvl_click, self.pvl)
		self.Bind(wx.EVT_BUTTON, self.uplat_click, self.uplat)
		self.Bind(wx.EVT_BUTTON, self.pv5_click, self.pv5)
		self.Bind(wx.EVT_BUTTON, self.upv5_click, self.upv5)
		self.Bind(wx.EVT_BUTTON, self.pv4_click, self.pv4)
		self.Bind(wx.EVT_BUTTON, self.upv4_click, self.upv4)
		self.Bind(wx.EVT_CLOSE, self.CLOSED, self)

	def pvl_click(self, event):
		userpath = os.path.expanduser('~')
		v6pathj = userpath + '/.cache/mindustrylauncher/v6/m.jar'
		print("Launching Latest Version")
		os.system("java -jar " + v6pathj)
		event.Skip()

	def uplat_click(self, event):
		userpath = os.path.expanduser('~')
		v6pathj = userpath + '/.cache/mindustrylauncher/v6/m.jar'
		v6path = userpath + "/.cache/mindustrylauncher/v6"
		url8 = "https://github.com/Anuken/Mindustry/releases/download/v121.4/Mindustry.jar"
		url7 = "https://github.com/Anuken/Mindustry/releases/download/v121.5/Mindustry.jar"
		url6 = "https://github.com/Anuken/Mindustry/releases/download/v122/Mindustry.jar"
		url5 = "https://github.com/Anuken/Mindustry/releases/download/v122.1/Mindustry.jar"
		url4 = "https://github.com/Anuken/Mindustry/releases/download/v122.2/Mindustry.jar"
		url3 = "https://github.com/Anuken/Mindustry/releases/download/v123/Mindustry.jar"
		url2 = "https://github.com/Anuken/Mindustry/releases/download/v123.1/Mindustry.jar"
		url1 = "https://github.com/Anuken/Mindustry/releases/download/v123.2/Mindustry.jar"
		try:
			urllib.request.urlretrieve(url8, v6pathj)
			print('Downloaded V6')
		except OSError as error:
			os.remove(v6pathj)
			urllib.request.urlretrieve(url8, v6pathj)
			print('Downloaded V6')
		except OSError as error:
			os.makedirs(v6path)
			urllib.request.urlretrieve(url8, v6pathj)
			print('Downloaded V6')
		except:
			print("Failed to download")
		event.Skip()

	def pv5_click(self, event):
		userpath = os.path.expanduser('~')
		v5pathj = userpath + "/.cache/mindustrylauncher/v5/m.jar"
		print("Launching V5")
		os.system("java -jar " + v5pathj)
		event.Skip()

	def upv5_click(self, event):
		urlv5 = 'https://github.com/Anuken/Mindustry/releases/download/v104.6/Mindustry.jar'
		userpath = os.path.expanduser('~')
		v5path = userpath + "/.cache/mindustrylauncher/v5"
		v5pathj = userpath + "/.cache/mindustrylauncher/v5/m.jar"
		try:
			urllib.request.urlretrieve(urlv5, v5pathj)
			print('Downloaded V5')
		except OSError as error:
			os.remove(v5pathj)
			urllib.request.urlretrieve(urlv5, v5pathj)
			print('Downloaded V5')
		except OSError as error:
			os.makedirs(v5path)
			urllib.request.urlretrieve(urlv5, v5pathj)
			print('Downloaded V5')
		except:
			print("Failed to download")
		event.Skip()

	def pv4_click(self, event):
		userpath = os.path.expanduser('~')
		v4pathj = userpath + "/.cache/mindustrylauncher/v4/m.jar"
		print("Launching V4")
		os.system("java -jar " + v4pathj)
		event.Skip()

	def upv4_click(self, event):
		urlv4 = 'https://github.com/Anuken/Mindustry/releases/download/v96/Mindustry.jar'
		userpath = os.path.expanduser('~')
		v4path = userpath + "/.cache/mindustrylauncher/v4"
		v4pathj = userpath + "/.cache/mindustrylauncher/v4/m.jar"
		try:
			urllib.request.urlretrieve(urlv4, v4pathj)
			print('Downloaded V4')
		except OSError as error:
			os.remove(v4pathj)
			urllib.request.urlretrieve(urlv4, v4pathj)
			print('Downloaded V4')
		except OSError as error:
			os.makedirs(v4path)
			urllib.request.urlretrieve(urlv4, v4pathj)
			print('Downloaded V4')
		except:
			print("Failed to download")
		event.Skip()

	def CLOSED(self, event):
		sys.exit("Exited Sucessfully")
		event.Skip()

# end of class MAINAPP

class downframe(wx.Frame):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.SetSize((164, 48))
		self.SetTitle("Download Complete")

		label_1 = wx.StaticText(self, wx.ID_ANY, "DOWNLOAD COMPLETE")
		self.Layout()
		self.Centre()

# end of class downframe

class MINDUSTRYLAUNCHER(wx.App):
	def OnInit(self):
		self.window = MAINAPP(None, wx.ID_ANY, "")
		self.SetTopWindow(self.window)
		self.window.Show()
		return True

# end of class MINDUSTRYLAUNCHER

if __name__ == "__main__":
	APP = MINDUSTRYLAUNCHER(0)
	APP.MainLoop()
