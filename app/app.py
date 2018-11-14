#!"C:\Python27\python.exe
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, session, url_for
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


@app.route('/new_user', methods = ['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        user = request.form["user"] 
        password = request.form["pass"]
        ciudad = request.form["ciudad"]

        if(insert_user(user, password, ciudad)):
            print "Usuario creado:  " + user
            return redirect(url_for('home'))
        else:
            session['error'] = 'Error al registrar usuario'
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
    if request.method == 'POST':
        idCiudad = request.form["ciudad"] 

        idUsuario = session['usuario']['idUsuario']

        if(update_city(idUsuario, idCiudad)):
            print "Ciudad modificada:  " + session['usuario']['ciudad'] + " en user: " + session['usuario']['usuario']
            return redirect(url_for('home'))
        else:
            session['error'] = 'Error al modificar la ciudad'
            return redirect(url_for('home'))

@app.route('/search_city', methods = ['POST', 'GET'])
def search_city():
    if request.method == 'GET':
        city = str(request.args.get('ciudad'))

        forecast = get_forecast_all(city)

        print forecast[0]['ciudad']
        print forecast[0]['pais']

        return render_template('forecast.html', **locals())
            
            

if __name__ == "__main__":
    app.debug = True
    app.run()
