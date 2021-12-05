import os

import speech_recognition as sr
import pyaudio

rec = sr.Recognizer()
# print(sr.Microphone.list_microphone_names())
texto = 'frase aleatoria'
with sr.Microphone() as mic:
    while texto != 'sair':
        rec.adjust_for_ambient_noise(mic)
        print("Fale agora")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto.lower())
        if texto == 'abrir chrome':
            print('Abriu o Chorme')
            os.system("start Chrome.exe")




