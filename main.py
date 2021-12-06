import os
import speech_recognition as sr
import pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def ouvir_microfone(frase=None):
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        while(frase != 'sair'):
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
            # cria_audio(frase)
        return frase

def justplay(aud):
    playsound(aud)

#Funcao responsavel por falar
def cria_audio(audio):
    global count
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save(f'hello{count}.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    justplay(f'hello{count}.mp3')
    count = count + 1

count = 1
ouvir_microfone()
