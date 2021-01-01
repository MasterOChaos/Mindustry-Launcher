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
		v6pathj = 'v6.jar'
		print("Launching Latest Version")
		os.system("java -jar " + v6pathj)
		event.Skip()

	def uplat_click(self, event):
		v6pathj = 'v6.jar'
		urlend1 = '/Mindustry.jar'
		urlend2 = '.1/Mindustry.jar'
		urlend3 = '.2/Mindustry.jar'
		urlend4 = '.3/Mindustry.jar'
		urlend5 = '.4/Mindustry.jar'
		urlend6 = '.5/Mindustry.jar'
		coreurl1 = 'https://github.com/Anuken/Mindustry/releases/download/v122'
		coreurl2 = 'https://github.com/Anuken/Mindustry/releases/download/v123'
		coreurl3 = 'https://github.com/Anuken/Mindustry/releases/download/v124'
		coreurl4 = 'https://github.com/Anuken/Mindustry/releases/download/v125'
		coreurl5 = 'https://github.com/Anuken/Mindustry/releases/download/v126'
		url30 = coreurl1 + urlend1
		url29 = coreurl1 + urlend2
		url28 = coreurl1 + urlend3
		url27 = coreurl1 + urlend4
		url26 = coreurl1 + urlend5
		url25 = coreurl1 + urlend6
		url24 = coreurl2 + urlend1
		url23 = coreurl2 + urlend2
		url22 = coreurl2 + urlend3
		url21 = coreurl2 + urlend4
		url20 = coreurl2 + urlend5
		url19 = coreurl2 + urlend6
		url18 = coreurl3 + urlend1
		url17 = coreurl3 + urlend2
		url16 = coreurl3 + urlend3
		url15 = coreurl3 + urlend4
		url14 = coreurl3 + urlend5
		url13 = coreurl3 + urlend6
		url12 = coreurl4 + urlend1
		url11 = coreurl4 + urlend2
		url10 = coreurl4 + urlend3
		url9 = coreurl4 + urlend4
		url8 = coreurl4 + urlend5
		url7 = coreurl4 + urlend6
		url6 = coreurl5 + urlend1
		url5 = coreurl5 + urlend2
		url4 = coreurl5 + urlend3
		url3 = coreurl5 + urlend4
		url2 = coreurl5 + urlend5
		url1 = coreurl5 + urlend6
		##here comes the execption handling
		def a1():
			try:
				urllib.request.urlretrieve(url1, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url1, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")
		def a2():
			try:
				urllib.request.urlretrieve(url2, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url2, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a3():
			try:
				urllib.request.urlretrieve(url3, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url3, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a4():
			try:
				urllib.request.urlretrieve(url4, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url4, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a5():
			try:
				urllib.request.urlretrieve(url5, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url5, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a6():
			try:
				urllib.request.urlretrieve(url6, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url6, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a7():
			try:
				urllib.request.urlretrieve(url7, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url7, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a8():
			try:
				urllib.request.urlretrieve(url8, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url8, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a9():
			try:
				urllib.request.urlretrieve(url9, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url9, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a10():
			try:
				urllib.request.urlretrieve(url10, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url10, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a11():
			try:
				urllib.request.urlretrieve(url11, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url11, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a12():
			try:
				urllib.request.urlretrieve(url12, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url12, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a13():
			try:
				urllib.request.urlretrieve(url13, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url13, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a14():
			try:
				urllib.request.urlretrieve(url14, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url14, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a15():
			try:
				urllib.request.urlretrieve(url15, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url15, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")
		def a16():
			try:
				urllib.request.urlretrieve(url16, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url16, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a17():
			try:
				urllib.request.urlretrieve(url17, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url17, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a18():
			try:
				urllib.request.urlretrieve(url18, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url18, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a19():
			try:
				urllib.request.urlretrieve(url19, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url19, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a20():
			try:
				urllib.request.urlretrieve(url20, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url20, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a21():
			try:
				urllib.request.urlretrieve(url21, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url21, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a22():
			try:
				urllib.request.urlretrieve(url22, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url22, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a23():
			try:
				urllib.request.urlretrieve(url23, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url23, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a24():
			try:
				urllib.request.urlretrieve(url24, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url24, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a25():
			try:
				urllib.request.urlretrieve(url25, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url25, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a26():
			try:
				urllib.request.urlretrieve(url26, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url26, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a27():
			try:
				urllib.request.urlretrieve(url27, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url27, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a28():
			try:
				urllib.request.urlretrieve(url28, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url28, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a29():
			try:
				urllib.request.urlretrieve(url29, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url29, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		def a30():
			try:
				urllib.request.urlretrieve(url30, v6pathj)
				print('Downloaded V6')
			except OSError as error:
				os.remove(v6pathj)
				urllib.request.urlretrieve(url30, v6pathj)
				print('Downloaded V6')
			except:
				print("Failed to download")

		for func in [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30]: # change list order to change execution order.
			try:
				func()
				print("eh it worked i guess")
				break
			except Exception as err:
				print("Hey this url doesn't exist yet")
				print (err)
				continue

	def pv5_click(self, event):
		v5pathj = "v5.jar"
		print("Launching V5")
		os.system("java -jar " + v5pathj)
		event.Skip()

	def upv5_click(self, event):
		urlv5 = 'https://github.com/Anuken/Mindustry/releases/download/v104.6/Mindustry.jar'
		v5pathj = "v5.jar"
		try:
			urllib.request.urlretrieve(urlv5, v5pathj)
			print('Downloaded V5')
		except OSError as error:
			os.remove(v5pathj)
			urllib.request.urlretrieve(urlv5, v5pathj)
			print('Downloaded V5')
		except:
			print("Failed to download")
		event.Skip()

	def pv4_click(self, event):
		v4pathj = "v4.jar"
		print("Launching V4")
		os.system("java -jar " + v4pathj)
		event.Skip()

	def upv4_click(self, event):
		urlv4 = 'https://github.com/Anuken/Mindustry/releases/download/v96/Mindustry.jar'
		v4pathj = "v4.jar"
		try:
			urllib.request.urlretrieve(urlv4, v4pathj)
			print('Downloaded V4')
		except OSError as error:
			os.remove(v4pathj)
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
