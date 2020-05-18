from flask import Flask #Função Flask do pacote flask
app = Flask(__name__) #Nome da aplicação

@app.route("/") #Raiz da app
def index():
	return "Index!"

@app.route("/hello") #São diferentes rotas da app, legal, gostei 
def hello():
	return "Hello World"

@app.route("/members")
def members():
	return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
	return name

#Para rodar:
if __name__ == "__main__":
	app.run()


