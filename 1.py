import warnings
import json
warnings.filterwarnings("ignore")
import sys

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# import kivy  # importing main package
# from kivy.app import App  # required base class for your app.
# from kivy.uix.label import Label  # uix element that will hold text
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
# from kivy.uix.image import Image

# kivy.require("1.10.1")  # make sure people running py file have right version

# Our simple app. NameApp  convention matters here. Kivy
# uses some magic here, so make sure you leave the App bit in there!

# class RecPage(GridLayout):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)

#         self.cols =1

#         self.texture = Image(source='logo.jpeg').texture
        

#         self.btn=Button(text="Recognize")
#         self.btn.bind(on_press=self.recbtn)
#         self.add_widget(Label())
#         self.add_widget(self.btn)


    # def recbtn(self, instance):
# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SQLITE_SAMPLE") as f:
    config = json.load(f)

        #create a Dejavu instance
    djv = Dejavu(config)
	# # Or recognize audio from your microphone for `secs` seconds
#    self.add_widget(Label(text="recording started"))
    secs=4
    song = djv.recognize(MicrophoneRecognizer, seconds=secs)
    if song is None:
        print("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
        sys.stdout.flush()
    else:
        print("'%d  %s  %s  %s  %s  %s  %s'" % (secs, song['song_id'],song['song_name'],song['confidence'],song['offset'],song['offset_seconds'],song['file_sha1']))
        sys.stdout.flush()
        
# class EpicApp(App):
# This is your "initialize" for the root wiget
    # def build(self):
        # Creates that label which will just hold text.
        # return RecPage()



# Run the app.
# if __name__ == "__main__":
#     EpicApp().run()
