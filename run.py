"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
	return "<h1>¡Hola mundo! :)</h1>"
	return "<h2>Por: Jdesparza</h2>"

@app.route('/suma')
def suma():
	resultado = 10 + 10
	return "<h3>10 + 10 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
	provincias = ["Esmeraldas", "Manabí", "Los Ríos", "Santa Elena", "Guayas"]
	capitales = ["Esmeraldas", "Portoviejo", "Babahoyo", "Santa Elena", "Guayaquil"]

	ecuador = ""

	for provincia, capital in zip (provincias, capitales):
		ecuador = "%s<h3>Provincia= %s - Capital= %s\n</h3>" % (ecuador, provincia, capital)
	
	return ecuador 

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8000, debug=True)
