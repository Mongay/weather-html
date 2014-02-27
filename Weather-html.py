#coding: utf-8 

import requests
import json
import webbrowser
from jinja2 import Template

ciudades = ['Almeria','Cadiz','Cordoba',Granada','Huelva','Malaga','Jaen','Sevilla']


plantilla = open('plantilla.html','r')
html = ''
for linea in plantilla:

	html += linea
plantilla = Template(html)

temp_minima = []
temp_maxima = []
vel_viento = []
direc_viento = []

for ciudad in ciudades:
	resultado = request.get('http:/api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' %ciudades[ciudad]})
	direccion = json.loads(resultado.text)

	if dicc == {u'message': u'Error: Not found city', u'cod': u'404'}:

		acceso = false
		temp_minima = ''
		temp_maxima = ''
		velo_viento = ''
		direc_viento = ''

	if acceso == True:

		minima = round(dicc["main"]["temp_minima"] - 273)
		maxima = round(dicc["main"]["temp_maxima"] - 273)
		velocidad = round(dicc["wind"]["speed"] * 1,6)
		direccion = dicc["wind"]["deg"]

	for grado in str(direccion):
		
		if direccion = 0 or direccion = 360:
			return "Norte"
		elif direccion = 180:
			return "Sur"
		elif direccion = 90:
			return "Este"
		elif direccion = 270:
			return "Oeste"
		elif direccion > 0 and direccion < 90:
			return "Noreste"
		elif direccion > 90 and direccion < 180:
			return "Sureste"
		elif direccion > 180 and direccion < 270:
			return "Suroeste"
		elif direccion > 270 and direccion < 360:
			return "Noroeste"


		temp_minima.append(minima)
		temp_maxima.append(maxima)
		vel_viento.append(velocidad)
		direc_viento.append(direccion)

	acceso = True

Tiempo = plantilla.render(ciudades=ciudades,temp_minima=minima,temp_maxima=maxima,vel_viento=velocidad,direc_viento=direccion)
archivo = open('tiempo.html','w')
archivo.write(tiempo)
archivo.close()
webbrowser.open("tiempo.html")
