from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/") #Claro, porque sempre o endereço já vem acompanhado de uma barra
def index():
	return "Flask App!"

@app.route("/hello/<string:name>/") #Alimentação do arquivo html
def hello(name):
	return render_template("template2.html",name=name)

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 80)

	#ip do host: 0.0.0.0 e porta 80 (padrão de servidores web)