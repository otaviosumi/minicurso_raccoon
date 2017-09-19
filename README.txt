Para ativar:
$ virtualenv -p python3 env
$ source env/bin/activate

Para verificar instalados:
$ pip freeze

Para instalar:
$ pip install flask mongoengine

Para desativar:
$ deactivate

data = {'name': 'lalala', 'email': 'lala@lala.com'}
req = request.post('http://localhost:5000/users', json=data)

