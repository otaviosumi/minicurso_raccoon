#https://education.github.com/pack

from flask import Flask, request
import mongoengine as me
import json

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
	user = me.ReferenceField(User)
	color = me.StringField()





app = Flask(__name__)

@app.route("/users", methods = ['GET'])
def get_users():
	users = User.objects.all()
	array = []
	for user in users:
		array.append({
			'id' : str(user._id),
			'name' : user.name,
			'email' : user.email
			})
	return 

if __name__ == "__main__":
	app.run()