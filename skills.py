import os
import webbrowser
import sys
import subprocess

import voice

try:
	import requests		#pip install requests
except:
	voice.speaker('ебанное говно')

def browser():
	webbrowser.open('https://www.youtube.com', new=2)


def game():
	try:
		subprocess.Popen('C:/Users/Павел/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
	except:
		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():

	os.system('shutdown /s')


def weather():
	try:
		params = {'q': 'Lipetsk', 'units': 'metric', 'lang': 'ru', 'appid': 'cc36700eb642ef4ebcb7a62836255d0a'}
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		if not response:
			raise
		w = response.json()
		voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	except:
		voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
	'''Отключает бота'''
	sys.exit()


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass

