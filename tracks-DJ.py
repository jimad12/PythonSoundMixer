#!/usr/bin/python

from Tkinter import *
from sound_DjMix import *
import pygame.mixer
import os

"""
DJ Application For Mixing Tracks

"""

app = Tk()
app.title("Tracks Sound Mix")
app.geometry("650x400+300+300")


#start the sound system
mixer = pygame.mixer 
mixer.init()

bodyTxt = Label(app, text="Cool DJ Sound Tracks Mixer", height=3, background ="green")
bodyTxt.pack( padx= 10, pady =10)

#get the names of all the files in the current directory
dirList = os.listdir(".")
for fname in dirList:
  if fname.endswith("wav"):
    DjMix = SoundMixer(app, mixer, fname)
    DjMix.pack()

  
#Capture Other window events to stop the track when the user click x to close gui before stoping it
def shutdown():
  #track.stop()
  app.destroy() #will close the gui window  



#Call app.protocol() before the call to app.mainloop() "Shutdown() function above"
app.protocol("WM_DELETE_WINDOW", shutdown)

#Start The Gui Event Loop.
app.mainloop()