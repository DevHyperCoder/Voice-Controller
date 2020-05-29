# gTTS is imported for "Text to Speech" conversion
from gtts import gTTS 
import os 
  
# The text that you want to convert to audio 
mytext = 'Hi How are you? Hope this works for you!'
  
# Language in which you want to convert 
language = 'en'
  
# You can change slow to True if you want
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("test.mp3") 
  
# Playing the converted file 
os.system("mpg321 test.mp3") 