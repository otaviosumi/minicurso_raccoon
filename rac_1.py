#https://education.github.com/pack

from flask import Flask
import mongoengine as me

class User(me.Document):
	name = me.StringField()
	email = me.StringField()

class Task(me.Document):
	description = me.StringField()
	desdline = me.DateTimeField()
	added = me.DateTimeField()
	title = me.StringField()
	finished = me.BooleanField()
	tags = me.ListField(me.StringField())
	images = me.ListField(me.StringField())




app = Flask(__name__)

@app.route("/sumi")
def hello():
	return "hello sumi-san"

if __name__ == "__main__":
	app.run()