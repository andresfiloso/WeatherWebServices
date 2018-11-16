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

	cur = get_cur(datasource)

	sql = ("SELECT * FROM usuario WHERE usuario = '" + user + "' AND password = '" + password + "'")
	print sql
	rows = cur.execute(sql)

	usuario = ""
	ciudad = ""
	idCiudad = ""

	for row in cur:

		idUsuario = row[0]
		usuario = row[1]
		idCiudad = str(row[3])
		
	
	sql = ("SELECT ciudad FROM ciudad WHERE idCiudad = " + idCiudad)
	print sql
	rows = cur.execute(sql)
	
	for row in cur:

		ciudad = row[0]
		print "encontro la ciudad: " + ciudad		

	usuario = {
			'idUsuario': idUsuario, 
			'usuario' : usuario,
			'ciudad' : ciudad,
			}

	session['usuario'] = usuario

	return rows

	
def insert_user(user, password, ciudad):
	print "Hola entre en el controller piola"
	
	sql = ("INSERT INTO `usuario` (`usuario`, `password`, `idCiudad`) VALUES ('"+user+"', '"+password+"', '"+ciudad+"');")
	print sql
	rows = get_cur(datasource).execute(sql)
	get_db(datasource).commit()
	return rows

def update_city(idUsuario, idCiudad):
	sql = ("UPDATE `usuario` SET `idCiudad` = '" + str(idCiudad) + "' WHERE `usuario`.`idUsuario` = '" + str(idUsuario) + "';")
	rows = get_cur(datasource).execute(sql)
	get_db(datasource).commit()

	ciudad = ""

	cur = get_cur(datasource)
	sql = ("SELECT ciudad FROM ciudad WHERE idCiudad = " + str(idCiudad))
	print sql
	rows = cur.execute(sql)

	for row in cur:
		ciudad = row[0]

	usuario = session['usuario']['usuario']

	session.clear()

	updated_user={}

	updated_user = {
			'idUsuario': idUsuario, 
			'usuario' : usuario,
			'ciudad' : ciudad,
			}

	session['usuario'] = updated_user

	return rows

def get_cities():

	cur = get_cur(datasource)

	sql = ("SELECT * FROM ciudad")
	rows = cur.execute(sql)

	ciudades = {}
	i = 0

	for row in cur.fetchall():

		ciudad = {
			'idCiudad': row[0], 
			'ciudad' : unicode(row[1], errors='replace'),
			'codigo_ciudad' : row[2],
			'latitud' : row[3],
			'longitud' : row[4],
			}

		ciudades[i] = ciudad

		i += 1

	
	
	with open('data/ciudades.json', 'w') as file:
		json.dump(ciudades, file)


def select_cities(ciudad):

	cur = get_cur(datasource)

	sql = ("SELECT * FROM ciudad where ciudad LIKE '"+ ciudad +"%' LIMIT 5")
	rows = cur.execute(sql)

	ciudades = {}
	i = 0

	for row in cur.fetchall():

		ciudad = {
			'idCiudad': row[0], 
			'ciudad' : unicode(row[1], errors='replace'),
			'codigo_ciudad' : row[2],
			'latitud' : row[3],
			'longitud' : row[4],
			}

		ciudades[i] = ciudad

		i += 1

	return ciudades
		
def get_current_city(city):
	current_data = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + key + '&units=metric' # full url

	req = requests.get(current_data)
	current = json.loads(req.text)

	#print city
	#print current_data
	#print req.text


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
	pais = forecast['city']['country']
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
			'pais': pais, 
			'icon': icon,
		}

		mediciones[i] = m

		i += 1
		
	return mediciones


def get_mediciones_principales(): # la idea seria que no pase parametros. que dentro del procedimiento vaya a buscar tambien las ciudades mas visitadas de forma independiente
	mediciones_principales = {}

	ciudades = get_main_citys()

	#print ciudades

	#print len(ciudades)

	for i in range(len(ciudades)):
		mediciones_principales[i] = get_current_city(ciudades[i])

	#print mediciones_principales

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

	#print ciudades
	return ciudades


def get_forecast_avg(city):
	mediciones = get_forecast_all(city)
	mediciones_avg = []

	datetime_today = datetime.today()
	dia = datetime_today.day

	minimo = 200
	maximo = -200

	dia0 = dia
	dia1 = dia+1
	dia2 = dia1+1
	dia3 = dia2+1
	dia4 = dia3+1
	dia5 = dia4+1

	print "Hoy: " + str(dia0)
	print "tomorrow: " + str(dia1)
	print "tomorrow +1 : " + str(dia2)
	print "tomorrow +2 : " + str(dia3)
	print "tomorrow +3 : " + str(dia4)
	print "tomorrow +4 : " + str(dia5)


	evDay = dia0

	i = 0

	for key in mediciones:

		name = mediciones[key]['ciudad']
		pais = mediciones[key]['pais']

		datetime_medicion = datetime.strptime(mediciones[key]['hora'], '%Y-%m-%d %H:%M:%S')

		fecha = datetime_medicion.strftime("%d-%m-%Y")
 
		print  fecha

		if(datetime_medicion.day == evDay):
			print "Encontre la fecha a evaluar....."

			temp_min = mediciones[key]['temp_min']
			temp_max = mediciones[key]['temp_max']

			if(temp_min < minimo):
				minimo = temp_min
			if(temp_max > maximo):
				maximo = temp_max
				icon = str(mediciones[key]['icon']) # se va a tomar como icono del dia el que corresponde a la mayor temperatura


			print "Medicion: " + str(datetime_medicion.hour) 
			print "Hasta ahora la temperatura maxima del primer dia es: " + str(maximo)
			print "Hasta ahora la temperatura minima del primer dia es: " + str(minimo)
			print "-------------"

			m = {
			'ciudad' : name,
			'fecha' : fecha, 
			'temp_min' : minimo,
			'temp_max' : maximo, 
			'pais': pais, 
			'icon': icon,
			}

			print "hasta ahora lo que voy a mostrar para esta fecha es: " + str(m)


			print "Evday = : " + str(evDay)
			print "dia5: " + str(dia5)
			print ""

			if(evDay == dia5 and datetime_medicion.hour == 18):
				mediciones_avg.append(m)
				return mediciones_avg

		else:
			print "La fecha es distinta...."
			minimo = 200
			maximo = - 200

			print "VALOR DE I -------------------------------------------- > " + str(i)
			if(i <= 5):
				print "valor de i: " + str(i)
				print "Pasamos a la proxima fecha: "
				mediciones_avg.append(m)
				print "Hasta ahora las mediciones a pasar son estas: " + str(mediciones_avg)
				evDay = evDay + 1

				print "-----------------------------------"
				print "Ahora vamos a ir por el dia: " + str(evDay)
				i += 1
				







		
	

	
