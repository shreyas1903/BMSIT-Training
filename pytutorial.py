print("wow working")

from playsound import playsound
from gtts import gTTS
import os
MsgVar = "hello bhosadiwaale shashank, learning gtts with madarchodh shashank"
GttsVar = gTTS(text=MsgVar,lang='en')

GttsVar.save("Gts.mp3")




playsound("Gts.mp3")