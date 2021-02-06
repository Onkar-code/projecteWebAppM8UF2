from flask import Flask, Blueprint, render_template

app = Flask(__name__)
auth = Blueprint('auth',__name__)

user = 'user'
pwd = '1234'

@app.route('/', methods=['POST'])
def login_post():
	return render_template('index.html')	
	user_post = request.form.get('user')
	pwd_post = request.form.get('pwd')
	print(user_post)
	print(pwd_post)
	if user != user_post or pwd != pwd_post:
		print('Please try again')
		#return render_template('index.html')	
	return render_template('calc.html')

#@app.route('/',)
#def home():
#	return render_template('index.html')	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
	

