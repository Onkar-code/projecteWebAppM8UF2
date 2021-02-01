from flask import Flask, render_template,jsonify

app = Flask(__name__)

#mapping URLs to functions

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suma/<param1>/<param2>')
def suma(param1, param2)
    n_param1 = float(param1)
    n_param2 = float(param2)
    resultat = {'resultat':n_param1+n_param2}
    return jsonify(resultat), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')