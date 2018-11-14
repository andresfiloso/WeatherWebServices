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
    if session.get('isLogged') is not None:

        city = 'banfield'  # id for Banfield
          # api key
        current_weather = get_current_city(city)

        forecast = get_forecast_all(city)


        return render_template('mainView.html', **locals()) #**locals() pasa todos las variables utilizadas a la vista
    else:
        #error = "Session Timeout"

        mediciones_principales = get_mediciones_principales() # la idea seria que no pase parametros. que dentro del procedimiento vaya a buscar tambien las ciudades mas visitadas de forma independiente

        get_main_citys()

        return render_template('login.html', **locals())


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

@app.route('/search_city', methods = ['POST', 'GET'])
def search_city():
    if request.method == 'GET':
        city = request.args.get('ciudad')

        forecast = get_forecast_all(city)

        print forecast[0]['ciudad']
        print forecast[0]['pais']

        return render_template('forecast.html', **locals())
            
            

if __name__ == "__main__":
    app.debug = True
    app.run()
