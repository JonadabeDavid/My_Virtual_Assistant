import os

import speech_recognition as sr
import pyaudio

def ouvir_microfone(frase=None):
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        while(frase != 'sair'):
            # microfone.adjust_for_ambient_noise(source)
            print('Pode Falar')

            try:
                frase = microfone.recognize_google(microfone.listen(source), language='pt-BR')
                # frase = microfone.recognize_google(audio, language='pt-BR')
                frase = frase.lower()
                print("Frase: " + frase)
                if frase == 'abrir chrome':
                    os.system("start Chrome.exe")
                    print('Abriu!!!')

            except sr.UnknownValueError:
                print("Não Entendi!")
        return frase

ouvir_microfone()



