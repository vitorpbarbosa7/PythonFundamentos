from flask import Flask

app = Flask(__name__)

@app.route("/") #Endereço da aplicação

def hello():
	return "Hello World"

if __name__ == "__main__":
	app.run() #Executar a aplicação

