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

        ciudades = ["Banfield", "Lomas de Zamora", "Avellaneda", "Amsterdam", "Rio de Janeiro"]
        mediciones_principales = get_mediciones_principales(ciudades) # la idea seria que no pase parametros. que dentro del procedimiento vaya a buscar tambien las ciudades mas visitadas de forma independiente

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

if __name__ == "__main__":
    app.debug = True
    app.run()
