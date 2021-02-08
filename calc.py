from flask import Flask, request, make_response, render_template, jsonify
from flask import request

app = Flask(__name__)

#mapping URLs to functions
credentials = {
	"user": "user",
	"password": "1234"
}

@app.route('/')
def login():
	if request.authorization and request.authorization.username == credentials["user"] and request.authorization.password== credentials["password"]:
		return render_template('calc.html')
	return make_response('No se ha podido verificar!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})
    
@app.route('/calc/suma/<param1>/<param2>')
def suma(param1, param2):
	n_param1 = float(param1)
	n_param2 = float(param2)
	resultat = {'resultat':n_param1+n_param2}
	return jsonify(resultat), 200

@app.route('/calc/resta/<param1>/<param2>')
def resta(param1, param2):
	n_param1 = float(param1)
	n_param2 = float(param2)
	operacio = n_param1 - n_param2
	resultat = {'resultat': operacio}   	
	return jsonify(resultat), 200
	
@app.route('/calc/multiplicacio/<param1>/<param2>')
def multiplicacio(param1, param2):
	n_param1 = float(param1)
	n_param2 = float(param2)
	resultat = {'resultat': n_param1 * n_param2}    
	return jsonify(resultat), 200
	
@app.route('/calc/divisio/<param1>/<param2>')
def divisio(param1, param2):
	n_param1 = float(param1)
	n_param2 = float(param2)
	
	if n_param1 == 0 and n_param2 == 0:
		operacio = 'indeterminado'
	elif(n_param2 == 0):
		operacio = 'infinito'
	else:
		operacio = n_param1 / n_param2
	
	resultat = {'resultat': operacio}    
	return jsonify(resultat), 200


if __name__ == '__main__':
    app.run(host='localhost', port='5000')
