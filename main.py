import eel
from config import TOKEN, LANGUAGE
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = LANGUAGE 

owm = OWM(TOKEN)

@eel.expose
def get_weather(city):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	temp = observation.weather.temperature('celsius')['temp']
	
	return f"В городе {city} сейчас {temp} градусов!"
	
	
# Вызов места хранения директории
eel.init("web ")

#Запуск библиотеки eel + указываем откуда и ставим размер окна.
eel.start("main.html", size=(700, 700))