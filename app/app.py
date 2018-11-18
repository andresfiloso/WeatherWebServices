#!"C:\Python27\python.exe
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, session, url_for, jsonify
from datasource import *
from controller import *

import os
import time

app = Flask(__name__)
app.secret_key = 'super secret key'

datasource = DataSource()

@app.route('/')
def default():
    return redirect(url_for('home'),code=307)

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/home', methods = ['POST', 'GET'])
def home():
    if session.get('usuario') is not None:

        city = session['usuario']['ciudad']
        print "Vamos a mostrar el menu principal. Esta es la ciudad del usuario: " + session['usuario']['usuario'] + ": " + session['usuario']['ciudad']    
          # api key
        current_weather = get_current_city(city)

        forecast = get_forecast_all(city)

        #data = get_cities()

        #ciudades = json.dumps(data)
        #print "=================================="
        #print ciudades

        return render_template('mainView.html', **locals()) #**locals() pasa todos las variables utilizadas a la vista
    else:
        #error = "Session Timeout"

        mediciones_principales = get_mediciones_principales() # la idea seria que no pase parametros. que dentro del procedimiento vaya a buscar tambien las ciudades mas visitadas de forma independiente

        get_main_citys()

        return render_template('login.html', **locals())


@app.route('/sign_up', methods = ['POST', 'GET'])
def sign_up():
    
    return render_template('sign_up.html', **locals())


@app.route('/new_user', methods = ['POST', 'GET', 'PUT'])
def new_user():
    if request.method == 'PUT':
        user = request.form["user"] 
        password = request.form["pass"]
        ciudad = request.form["ciudad"]

        print user
        print password
        print ciudad

        idCiudad = ciudad.split('-')[0]


        print "Id ciudad: " + str(idCiudad)


        if(insert_user(user, password, idCiudad)):
            print "Usuario creado:  " + user
            session['success'] = "Usuario creado con exito"
            return redirect(url_for('home'))
        else:
            session['error'] = 'Error al registrar usuario'
            return redirect(url_for('home'))
    else:
        print "No entro en el metodo"
        session['error'] = 'No entro en el method'
        return redirect(url_for('home'))


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form["user"] 
        password = request.form["pass"]

        if(auth_user(user, password)):
            print "Welcome " + user
            return redirect(url_for('home'))
        else:
            session['error'] = 'Usuario o clave incorrecta!'
            return redirect(url_for('home'))


@app.route('/change_city', methods = ['POST', 'GET'])
def change_city():
    if request.method == 'GET':
        ciudad = request.args.get('ciudad')

        print ciudad

        idUsuario = session['usuario']['idUsuario']

        idCiudad = ciudad.split('-')[0]

        print "Id ciudad: " + str(idCiudad)


        if(update_city(idUsuario, idCiudad)):
            print "Ciudad modificada:  " + session['usuario']['ciudad'] + " en user: " + session['usuario']['usuario']
            return redirect(url_for('home'))
        else:
            session['error'] = 'Error al modificar la ciudad'
            return redirect(url_for('home'))

@app.route('/change_city_view', methods = ['POST', 'GET'])
def change_city_view():
    return render_template('change_city.html', **locals())

@app.route('/delete_user_view', methods = ['POST', 'GET'])
def delete_user_view():
    return render_template('delete_user_view.html', **locals())


@app.route('/delete_user', methods = ['POST', 'GET', 'DELETE'])
def delete_user():
    if request.method == 'DELETE':
        user = request.form["user"] 
        password = request.form["pass"]

        if(drop_user(user, password)):
            session.clear()
            return redirect(url_for('home'))
        else:
            session['error'] = 'Error al eliminar usuario'
            return redirect(url_for('home'))
    else:
        print "No entro en el metodo"
        session['error'] = 'No entro en el method'
        return redirect(url_for('home'))

@app.route('/search_city', methods = ['POST', 'GET'])
def search_city():
    if request.method == 'GET':
        city = str(request.args.get('ciudad'))


        forecast = get_forecast_avg(city)

        print "-----------------------------------------------------"
        print "Estas son las mediciones a mostrar: " + str(forecast)

        print "-----------------------------------------------------"

        print "-----------------------------------------------------"

        print "-----------------------------------------------------"

        print "-----------------------------------------------------"


        for i in range(6):
            print forecast[i]['ciudad']
            print forecast[i]['temp_min']
            print forecast[i]['temp_max']
            print forecast[i]['icon']


        return render_template('forecast.html', **locals())
            

@app.route('/lookup_city', methods = ['POST', 'GET'])
def lookup_city():
    if request.method == 'GET':
        city = str(request.args.get('data'))

        print "CIUDAD: " + city

        cities = select_cities(city)

        print cities
          
        return jsonify(result=cities)
            

if __name__ == "__main__":
    app.debug = True
    app.run()
