import pyaudio
import speech_recognition 

from gtts import gTTS 
import os 
  
# Language in which you want to convert 
language = 'en'

recogniser = speech_recognition.Recognizer()



# TODO change the DEVICE_INDEX here!!!
DEVICE_INDEX = 0

mic = speech_recognition.Microphone(device_index=DEVICE_INDEX)

