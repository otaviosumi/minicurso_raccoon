#https://education.github.com/pack
#https://github.com/otaviosumi/minicurso_raccoon

from flask import Flask, request, jsonify
from datetime import datetime
import mongoengine as me
import json



#Classes######################################################
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
	deadline = me.DateTimeField()
	added = me.DateTimeField()
	title = me.StringField()
	finished = me.BooleanField()
	tags = me.ListField(me.StringField())
	user = me.ReferenceField(User)
	color = me.StringField()

	def to_dict(self):
		return{
				'id': str(self.id),
				'description': self.description,
				'deadline': self.deadline,
				'added': int(self.added.timestamp()),
				'title': self.title,
				'finished': int(self.added.timestamp()),
				'tags': self.tags,
				'user': self.user.id,
				'color': self.color,
		}


#main########################################################
#instancia flask
app = Flask(__name__)
#inicia banco de dados
me.connect('todo_app')

#User########################################################
#GET 
@app.route("/users", methods = ['GET'])
def get_users():
	users = User.objects.all()
	array = []
	for user in users:
		array.append(user.to_dict()) #recebe ele mesmo
	return jsonify(array)

#POST 
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

#Task########################################################
#GET 
@app.route("/tasks", methods = ['GET'])
def get_tasks():
	tasks = Task.objects.all()
	array = []
	for task in tasks:
		array.append(task.to_dict()) #recebe ele mesmo
	return jsonify(array)

#POST 
@app.route("/tasks", methods = ['POST'])
def create_task():
	if not request.is_json:
		return jsonify({'error' : 'nor_json'}), 400
	data = request.get_json()
	task = Task(finished=False, added=datetime.now())
	task.description = data.get('description')
	task.deadline = datetime.fromtimestamp(data.get('deadline', 0))
	task.title = data.get('title')
	task.tags = data.get('tags', [])
	task.user = User.objects.filter(id=data.get('user').first())
	task.color = data.get('color')
	task.save()
	return jsonify(task.to_dict())

if __name__ == "__main__":
	app.run(debug=True)