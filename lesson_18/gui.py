#! /usr/bin/env python

# should run "export VERSIONER_PYTHON_PREFER_32_BIT=yes"

import wx

try:
	with open('mydata.txt', 'r+') as data:
		myData = data.read()
except IOError:
	data = open('mydata.txt', 'w')
	myData = ''
	data.close()

def save(event):
	with open('mydata.txt', 'w') as data:
		data.write(textArea.GetValue())

app = wx.App()

frame = wx.Frame(None, title="hello world", size=(400, 400))
frame.Show()

helloButton = wx.Button(frame, label="save", pos=(160, 20), size=(80, 20))
helloButton.Bind(wx.EVT_BUTTON, save)

textArea = wx.TextCtrl(frame, style=wx.TE_MULTILINE, pos=(20, 100), size=(360, 250))
textArea.SetValue(myData)

app.MainLoop()