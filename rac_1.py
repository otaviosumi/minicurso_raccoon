#https://education.github.com/pack

from flask import Flask
import mongoengine as me

app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world!"

if __name__ == "__main__":
	app.run()