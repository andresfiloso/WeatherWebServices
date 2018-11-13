from flask import session
from datasource import *

datasource = DataSource()

#####################################################################
# DataSource es un objeto que permite el acceso a la base de datos.	#
# Informacion de esta clase en datasource.py 						#
#####################################################################

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
	