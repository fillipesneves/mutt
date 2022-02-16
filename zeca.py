import pyttsx3
# import engineio #engineio module is not needed.

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 150)    # Aquí puedes seleccionar la velocidad de la voz
engineio.setProperty('voice',voices[54].id)

pp = engineio.getProperty('voices')
count = 0
for x in pp:
	print(count)
	count = count+1
	print(x)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

speak("Olá, como posso ajudar")
while(1):
    phrase = input("--> ")
    if (phrase == "exit"):
        exit(0)
    speak(phrase)