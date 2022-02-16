from ouvir import *
from falar import *
from interagir import *
from time import sleep





while True:
    r = ouvir('Stand By')
    if "Zeca" in r or "zeca" in r:
        speak("Olá senhor, o que posso fazer ?")
        r = ouvir('Ouvindo')
        i = interagir(r)
        while i == 0:
            speak("Por favor, fale novamente o que precisa")
            r = ouvir('Ouvindo')          
            i = interagir(r)
            



