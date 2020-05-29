import pyaudio
import speech_recognition 

recogniser = speech_recognition.Recognizer()


# Check which one is your mic

print(speech_recognition.Microphone.list_microphone_names())

# in the print statement check which one is your mic and then change the variable to yours. 
# index starts at 0

DEVICE_INDEX = 0

mic = speech_recognition.Microphone(device_index=DEVICE_INDEX)

with mic as source:
    # Comment this out if there is no ambient noise
    r.adjust_for_ambient_noise(source)

    audio=recogniser.listen()

text = recogniser.recognize_google(audio)

print(text)



