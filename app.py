#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def welcome():
	#return "Hello, this is my 1st flask web app."
	name = ''
	food = ''
	if request.method == 'POST' and 'username' in request.form:
		name = request.form.get('username')
		food = request.form.get('userfood')
	return render_template('index.html', name = name, food = food)

# @app.route('/first', methods=['GET','POST'])
# def first():
# 	if request.method == 'POST':
# 		return 'POST: this is 1st page'
# 	else:
# 		return 'GET: this is 1st page'

# @app.route('/second')
# def second():
# 	return {"100":100,"200":200}

app.run()