from voice_controller import hear,speak
import control

def control(text):
    returnText = ""
    # Do all the checks here!!
    if "Hello" in text:
        returnText="Hello There! I am a robot"

    if "front" in text:
        # code to move front

    return returnText


print("Starting..")

while True:
    text = hear()
    
    # Some command to stop the loop 
    if "Stop" in text:
        break

    textToSpeak=control(text)

    if textToSpeak is "":
        # Probably some command. Continue the loop 
        continue

    speak(textToSpeak)

print("Stopping")


