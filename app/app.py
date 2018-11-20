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


@app.route('/home', methods = ['POST', 'GET', 'PUT'])
def home():
    if session.get('usuario') is not None:

        city = session['usuario']['ciudad']
        current_weather = get_current_city(city)

        forecast = get_forecast_all(city)

        return render_template('mainView.html', **locals()) #**locals() pasa todos las variables utilizadas a la vista
    else:
        #error = "Session Timeout"

        mediciones_principales = get_mediciones_principales() # la idea seria que no pase parametros. que dentro del procedimiento vaya a buscar tambien las ciudades mas visitadas de forma independiente

        get_main_citys()

        return render_template('login.html', **locals())


@app.route('/sign_up', methods = ['POST', 'GET'])
def sign_up():
    
    return render_template('sign_up.html', **locals())


@app.route('/new_user', methods = ['POST'])
def new_user():
    if request.method == 'POST':

        user = request.form["user"] 
        password = request.form["pass"]
        ciudad = request.form["ciudad"] 

        idCiudad = ciudad.split('-')[0]

        if(insert_user(user, password, idCiudad)):
            print "Usuario creado:  " + user
            session['success'] = "Usuario creado con exito"
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


@app.route('/change_city/<int:idCiudad>', methods = ['PUT'])
def change_city(idCiudad):
    if request.method == 'PUT':

        idUsuario = session['usuario']['idUsuario']

        if(update_city(idUsuario, idCiudad)):
            return "OK"
        else:
            session['error'] = 'Error al modificar la ciudad'
            return "ERROR"

@app.route('/change_city_view', methods = ['POST', 'GET'])
def change_city_view():
    return render_template('change_city.html', **locals())

@app.route('/delete_user_view', methods = ['POST', 'GET'])
def delete_user_view():
    return render_template('delete_user_view.html', **locals())


@app.route('/delete_user', methods = ['DELETE'])
def delete_user():
    if request.method == 'DELETE':

        usuario = session['usuario']['usuario']

        if(drop_user(usuario)):
            session.clear()
            session['success'] = 'Usuario fue dado de baja'
            return "OK"
        else:
            session['error'] = 'Error al eliminar usuario'
            return "ERROR"
    else:
        print "No entro en el metodo"
        session['error'] = 'No entro en el method'
        return redirect(url_for('home'))

@app.route('/search_city', methods = ['POST', 'GET'])
def search_city():
    if request.method == 'GET':
        city = str(request.args.get('ciudad'))
        forecast = get_forecast_avg(city)
        return render_template('forecast.html', **locals())
            

@app.route('/lookup_city', methods = ['POST', 'GET'])
def lookup_city():
    if request.method == 'GET':

        city = str(request.args.get('data'))
        cities = select_cities(city)     
        return jsonify(result=cities)
            

if __name__ == "__main__":
    app.debug = True
    app.run()
