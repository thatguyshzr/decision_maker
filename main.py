from flask import Flask, render_template, request
from decision_maker import *

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
	decision= ''
	counter= {}
	if request.method == 'POST':
		get_data= request.form.get('text_name')
		get_out_of= int(request.form.get('out_of'))
		if get_data == '':
			get_data= 'heads, tails'
		decision= decision_maker(get_data, get_out_of)
		counter= decision_counter(decision)

	return render_template('index.html', decision= decision,
							counter= counter)


if __name__ == '__main__':
    # app.run(debug=True, port= 5000)
    app.run(host='0.0.0.0')

