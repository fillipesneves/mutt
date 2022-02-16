import pyttsx3

robo = pyttsx3.init()
msg = input("Frase")
robo.say(msg)
robo.runAndWait()