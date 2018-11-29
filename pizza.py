from flask import * 

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/', methods=['POST'])
def main_post():
#test code
	fav_food = request.form.get('food')
	tf_val = request.form.get('truthy')
	if fav_food == 'pizza':
		return render_template('oops.html', message='You have good taste!')
	else:
		return render_template('main.html', message='That is not yummy.')

if __name__ == '__main__':
	app.run()