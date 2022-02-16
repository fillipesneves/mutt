from ouvir import *
from falar import *
from func import *
import threading
from threading import Thread
from datetime import datetime
import numero_por_extenso



def interagir(acao):
    if "resetar servidor" in acao:
        speak("Resetando servidores")
        os.popen('/srv/run/agenda.sh')
        speak("Pronto senhor.")
        speak("Foram reiniciados os servidores escravos, o proxy e o master.")
        return 1
    

    elif "Iniciar servidor" in acao or "iniciar servidor" in acao:
        speak("Tracar rota para qual endereço ?")
        resposta = ouvir('Ouvindo ...')
        os.popen('VBoxManage startvm '+resposta)
        return 1

    elif "hora"  in acao:
        data   = datetime.now().strftime('%d/%m/%Y %H:%M')
        hora   = datetime.now().strftime('%H')
        minuto = datetime.now().strftime('%M')
        hora   = numero_por_extenso.real(int(hora))
        minuto = numero_por_extenso.real(int(minuto))
        dizer = 'São '+hora+' horas'+' e '+minuto+' minutos'
        speak(dizer)
        return 1


    elif "Tocar"  in acao or "tocar" in acao:
        t1 = Thread(target= tocar, args=[])
        t1.start()
        return 1

    
    elif "mapear host" in acao:
        speak("Qual host deseja mapear ?")
        resposta = ouvir('Ouvindo ...')
        print("Mapeando "+str(resposta))
        speak("Mapeando "+str(resposta))
        mapearHost(resposta)
        return 1
    

    elif "tracar rota" in acao or "traçar rota" in acao or "Traçar rota" in acao:
        speak("Tracar rota para qual endereço ?")
        resposta = ouvir('Ouvindo ...')
        print("Traçando rota para "+str(resposta))
        speak("Traçando rota para "+str(resposta))
        tracarRota(resposta)
        return 1
    
    elif "mostrar rota" in acao or "Mostrar rota" in acao:
        mostrarRota()
        return 1

    else:
        speak("Não consegui entender")
        return 0


