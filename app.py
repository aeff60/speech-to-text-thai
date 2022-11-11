import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio, language="th"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))