# See https://github.com/contextio/Python-ContextIO for a guide
# this will be changed to flask syntax

from flask import Flask, render_template, request, url_for
import contextio as c
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('userLogin.html')

# contextio key and secret key ==> removed for security reasons
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

context_io = c.ContextIO(
    consumer_key=CONSUMER_KEY, 
    consumer_secret=CONSUMER_SECRET
)

if __name__ == '__main__':
	app.run(debug=True)
