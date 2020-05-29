from voice_controller import speech_recognition,recogniser,mic

def hear():
    with mic as source:
        # Comment this out if there is no ambient noise
        r.adjust_for_ambient_noise(source)

        audio=recogniser.listen()
        try:
            text = recogniser.recognize_google(audio)

            # Remove once in prod
            print(text)
        except:
            print("Please say again")
            text ="Please say again"


    return text