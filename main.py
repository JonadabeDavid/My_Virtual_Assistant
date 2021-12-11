import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
from pynput.keyboard import Key, Controller
import time
import pycaw
from subprocess import call



microfone = sr.Recognizer()
talker = pyttsx3.init()
keyb = Controller()

def use_voice(phrase=None):

    with sr.Microphone() as source:
        # microfone.adjust_for_ambient_noise(source)
        while(phrase != 'sair'):
            print('Pode Falar')

            try:
                phrase = microfone.recognize_google(microfone.listen(source), language='pt-BR')
                # phrase = microfone.recognize_google(audio, language='pt-BR')
                phrase = phrase.lower()
                voice_actions(phrase)

            except sr.UnknownValueError:
                print("Não Entendi!")
            except sr.RequestError:
                print("Erro de conexão")
            # cria_audio(phrase)
        talker.say('Saindo')
        talker.runAndWait()
        return phrase

# def getting_phrase(that_source):
#     try:
#         phrase = microfone.recognize_google(microfone.listen(that_source), language='pt-BR')
#         # phrase = microfone.recognize_google(audio, language='pt-BR')
#         phrase = phrase.lower()
#         voice_actions(phrase)
#
#     except sr.UnknownValueError:
#         print("Não Entendi!")

def voice_actions(phraseToDo):
    if 'maria' in phraseToDo:
        phraseToDo = phraseToDo.replace('maria', '')
        talker.say(phraseToDo)
        talker.runAndWait()
    print("phrase: " + phraseToDo)
    if 'abrir chrome' in phraseToDo:
        # talker.say('sim senhor jonadabe, meu mestre')
        # talker.runAndWait()
        os.system("start Chrome.exe")
    elif 'toque' in phraseToDo:
        music = phraseToDo.replace('toque', '')
        resultado = pywhatkit.playonyt(music)
        talker.say('Iniciando música')
        talker.runAndWait()
    elif 'fechar aba' in phraseToDo:
        # keyb.type('ola mundo')
        print('fechou')
        with keyb.pressed(Key.ctrl):
            keyb.press('w')
            keyb.release('w')
    elif 'pesquisar' in phraseToDo:
        keyb.press(';')
        keyb.release(';')
        with keyb.pressed(Key.ctrl):
            keyb.press('a')
            keyb.release('a')
        keyb.type(phraseToDo.replace('pesquisar', ''))
    elif phraseToDo == 'ok':
        keyb.press(Key.enter)
    elif phraseToDo == 'tela cheia':
        keyb.press('f')
    elif 'volume' in phraseToDo and 'para' in phraseToDo:
        a = []
        for s in phraseToDo.split():
            if s.isdigit():
                a.append(int(s))
        if 'dois' in phraseToDo:
            a.append(int(2))
        if a:
            set_volume(a[0])
        else:
            talker.say('Valor de volume não reconhecido')
            talker.runAndWait()
    elif 'assistente' in phraseToDo and 'funcionando' in phraseToDo:
        talker.say('Sim, estou funcionando')
        talker.runAndWait()



def set_volume(new_volume):
    for _ in range (50):
        keyb.press(Key.media_volume_down)
        time.sleep(0.0001)

    for _ in range (int(new_volume/2)):
        keyb.press(Key.media_volume_up)
        time.sleep(0.0001)

use_voice()
