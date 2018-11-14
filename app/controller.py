from flask import session, request, json
import requests
from datasource import *

from datetime import datetime

datasource = DataSource()

#####################################################################
# DataSource es un objeto que permite el acceso a la base de datos.	#
# Informacion de esta clase en datasource.py 						#
#####################################################################

key = '814c59b24b1da8eca1db0b0e28a04c1c'

import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def auth_user(user, password):
	
	if(user == "admin"):
		session['isLogged'] = user
		return 1

	"""
	cur = get_cur(datasource)

	sql = ("SELECT * FROM usuario where usuario = '" + user + "' and pass = '" + password + "'")
	rows = cur.execute(sql)

	for row in cur:
		usuario = Usuario(row['idUsuario'], row['usuario'], row['email'])
		session['usuario'] = usuario.getIdUsuario()
		return rows
	"""
	


def get_current_city(city):
	current_data = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + key + '&units=metric' # full url

	req = requests.get(current_data)
	current = json.loads(req.text)

	print city
	print current_data
	print req.text


	ciudad = current['name']
	temp = current['main']['temp']
	clima = current['weather'][0]['description']
	pais = current['sys']['country']
	icon = current['weather'][0]['icon']

	current_weather = {
			'ciudad' : ciudad,
			'temp' : temp,
			'clima' : clima, 
			'pais' : pais,
			'icon': icon,
	}

	return current_weather

def get_forecast_all(city):
	forecast_data = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&APPID=' + key + '&units=metric' # full url

	req = requests.get(forecast_data)
	forecast = json.loads(req.text)

	name = forecast['city']['name']
	mediciones = {}


	i = 0
	for medicion in forecast['list']:
		hora = str(medicion['dt_txt'])

		temp_min = medicion['main']['temp_min']
		temp_max = medicion['main']['temp_max']
		icon = str(medicion['weather'][0]['icon'])
		
		m = {
			'ciudad' : name,
			'hora' : hora, 
			'temp_min' : temp_min,
			'temp_max' : temp_max, 
			'icon': icon,
		}

		mediciones[i] = m

		i += 1
		
	return mediciones


def get_mediciones_principales(): # la idea seria que no pase parametros. que dentro del procedimiento vaya a buscar tambien las ciudades mas visitadas de forma independiente
	mediciones_principales = {}

	ciudades = get_main_citys()

	print ciudades

	print len(ciudades)

	for i in range(len(ciudades)):
		mediciones_principales[i] = get_current_city(ciudades[i])

	print mediciones_principales

	return mediciones_principales


def get_main_citys():
	cur = get_cur(datasource)

	sql = ("SELECT ciudad FROM ciudad ORDER BY cantidad_busquedas DESC LIMIT 5")
	rows = cur.execute(sql)

	ciudades = {}
	i = 0

	for row in cur.fetchall():
		ciudades[i] = row[0].decode('latin-1')
		i += 1

	print ciudades
	return ciudades


def get_forecast_avg(city):
	mediciones = get_forecast_all(city)


	datetime_today = datetime.today()
	dia = datetime_today.day

	minimo = 200
	maximo = -200


	for key in mediciones:

		name = mediciones[key]['ciudad']
		datetime_medicion = datetime.strptime(mediciones[key]['hora'], '%Y-%m-%d %H:%M:%S')

		if(datetime_medicion.day == dia):
			temp_min = mediciones[key]['temp_min']
			temp_max = mediciones[key]['temp_max']

			if(temp_min < minimo):
				minimo = temp_min
			if(temp_max > maximo):
				maximo = temp_max
				icon = str(mediciones[key]['icon']) # se va a tomar como icono del dia el que corresponde a la mayor temperatura


			print "Medicion: " + str(key) 
			print "Hasta ahora la temperatura maxima del " + str(datetime_medicion.strftime("%d/%m/%Y")) + " es: " + str(maximo)
			print "Hasta ahora la temperatura minima del " + str(datetime_medicion.strftime("%d/%m/%Y")) + " es: " + str(minimo)
			print "-------------"

		else:
			minimo = 200
			maximo = 200
			
			mediciones = {
				'ciudad' : name,
				'fecha' : datetime_medicion.strftime("%d/%m/%Y"), 
				'temp_min' : minimo,
				'temp_max' : maximo, 
				'icon': icon,
			}

			temp_min = mediciones[key]['temp_min']
			temp_max = mediciones[key]['temp_max']

			if(temp_min < minimo):
				minimo = temp_min
			if(temp_max > maximo):
				maximo = temp_max
				icon = str(mediciones[key]['icon']) # se va a tomar como icono del dia el que corresponde a la mayor temperatura
			datetime_medicion.day = dia


		
	

	
