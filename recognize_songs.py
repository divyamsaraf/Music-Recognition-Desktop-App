import warnings
import json
warnings.filterwarnings("ignore")


import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require("1.10.1")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
# with open("dejavu.cnf.SQLITE_SAMPLE") as f:
#     config = json.load(f)


class RecApp(App):
    def build(self):
        return Label(text="MUSIC RECOGNITION APP!")

        def recognizebtn(self):
                djv = Dejavu(config)
	# Or recognize audio from your microphone for `secs` seconds
		print("recording started")
		secs = 4
		song = djv.recognize(MicrophoneRecognizer, seconds=secs)
		if song is None:
			print("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
		else:
			print("From mic with %d seconds we recognized: %s\n" % (secs, song))

if __name__ == '__main__':
    RecApp().run
	
