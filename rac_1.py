#https://education.github.com/pack
#https://github.com/otaviosumi/minicurso_raccoon

from flask import Flask, request, jsonify
import mongoengine as me
import json

class User(me.Document):
	name = me.StringField()
	email = me.StringField()

	def to_dict(self):
		return {
				'id' : str(self.id),
				'name' : self.name,
				'email' : self.email,
				}

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
		array.append(user.to_dict()) #recebe ele mesmo
	return jsonify(array)


@app.route("/users", methods = ['POST'])
def create_user():
	if not request.is_json:
		return jsonify({'error' : 'nor_json'}), 400
	data = request.get_json()
	name = data.get('name')
	email = data.get('email')
	user = User(name=name, email=email)
	user.save()
	return jsonify(user.to_dict())


if __name__ == "__main__":
	app.run(debug=True)