import pygame
import pyttsx3

def tocar():
     pygame.mixer.init()
     pygame.mixer.music.load("/home/filipe/Música/Skank/Acima Do Sol.mp3")
     pygame.mixer.music.play()
     while pygame.mixer.music.get_busy() == True:
        continue



def speak(text):
    engineio = pyttsx3.init()
    voices = engineio.getProperty('voices')
    engineio.runAndWait()
    engineio.setProperty('rate', 178)          # velocidade da voz
    engineio.setProperty('gender', 'None')   # genero da voz
    engineio.setProperty('voice',voices[54].id)# ID referente a linguagem da voz
    engineio.say(text)
    engineio.runAndWait()
    engineio.stop()
 




