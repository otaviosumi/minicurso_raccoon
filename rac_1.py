#https://education.github.com/pack

from flask import Flask, request, jsonify
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

me.connect('todo_app')

@app.route("/users", methods = ['GET'])
def get_users():
	users = User.objects.all()
	array = []
	for user in users:
		array.append({
			'id' : str(user.id),
			'name' : user.name,
			'email' : user.email
			})
	return jsonify(array)

"""
@app.route("/users", methods = ['POST'])
def post_users():
	nome = #input de nome
	iemail = #input de email
	user = User(name = nome, email = iemail)
	user.save()
	return 
"""

if __name__ == "__main__":
	app.run()