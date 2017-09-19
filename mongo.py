import mongoengine as me

database_name = 'test'
me.connect (database_name)
#define tabela
class Car(me.Document):
	id = me.IntField(primary_key = True)
	model = me.StringField()
	color = me.StringField()
	year = me.IntField()

#insere
my_car = Car(
	id = 1,
	model = 'Fusca',
	color = 'yellow',
	year = 1962)
my_car.save()
#procura
result = Car.objects.filter(id=1).first()
print(result.model)