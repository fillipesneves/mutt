import speech_recognition as sr

import os

#Função para ouvir e reconhecer a fala
def ouvir(status):
    #Habilita o microfone do usuário
    #mic_name = "HDA Intel PCH: ALC257 Analog (hw:0,0)"
    microfone = sr.Recognizer()
    sample_rate = 48000
    chunk_size = 2048
    mic_list = sr.Microphone.list_microphone_names() # obtem a lista de microfones conectado
             

    
    #usando o microfone
    #with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        print(status)
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Retorna a frase pronunciada
        return frase
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except:
        return "0"
        

