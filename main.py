import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
from pynput.keyboard import Key, Controller
import time


microfone = sr.Recognizer()
talker = pyttsx3.init()
keyb = Controller()

def use_voice(frase=None):

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        while(frase != 'sair'):
            print('Pode Falar')

            try:
                frase = microfone.recognize_google(microfone.listen(source), language='pt-BR')
                # frase = microfone.recognize_google(audio, language='pt-BR')
                frase = frase.lower()
                voice_actions(frase)

            except sr.UnknownValueError:
                print("Não Entendi!")
            # cria_audio(frase)
        talker.say('Saindo')
        talker.runAndWait()
        return frase

# def getting_frase(that_source):
#     try:
#         frase = microfone.recognize_google(microfone.listen(that_source), language='pt-BR')
#         # frase = microfone.recognize_google(audio, language='pt-BR')
#         frase = frase.lower()
#         voice_actions(frase)
#
#     except sr.UnknownValueError:
#         print("Não Entendi!")

def voice_actions(fraseToDo):
    if 'maria' in fraseToDo:
        fraseToDo = fraseToDo.replace('maria', '')
        talker.say(fraseToDo)
        talker.runAndWait()
    print("Frase: " + fraseToDo)
    if 'abrir chrome' in fraseToDo:
        talker.say('sim senhor jonadabe, meu mestre')
        talker.runAndWait()
        os.system("start Chrome.exe")
    elif 'toque' in fraseToDo:
        music = fraseToDo.replace('toque', '')
        resultado = pywhatkit.playonyt(music)
        talker.say('Tocando música')
        talker.runAndWait()
    elif 'fechar aba' in fraseToDo:
        # keyb.type('ola mundo')
        print('fechou')
        with keyb.pressed(Key.ctrl):
            keyb.press('w')
            keyb.release('w')
    elif 'pesquisar' in fraseToDo:
        keyb.press(';')
        keyb.release(';')
        with keyb.pressed(Key.ctrl):
            keyb.press('a')
            keyb.release('a')
        time.sleep(0.25)
        keyb.type(fraseToDo.replace('pesquisar', ''))
        time.sleep(0.25)
        keyb.press(Key.enter)


use_voice()
