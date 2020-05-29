from voice_controller import gTTS  
def speak(text=""):
    # You can change slow to True if you want
    speaker = gTTS(text=mytext, lang=language, slow=False) 
    
    speaker.save("test.mp3") 
    
    os.system("mpg321 test.mp3") 
