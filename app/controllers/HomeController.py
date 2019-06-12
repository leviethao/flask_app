from flask import redirect, url_for, request

class HomeController():
    def __init__(self):
        pass
    
    def index(self):
        return 'Hello, this is Home page'

    def hello_user(self, name, age, score):
        return 'name: {name}, age: {age}, score: {score}'.format(name=name, age=age, score=score)

    def hello_admin(self):
        return 'hello admin'

    def hello_person(self, name):
        if name == 'admin':
            return redirect(url_for('routes.hello_admin'))
        else:
            return redirect(url_for('routes.hello_user', name=name, age=10, score=9.5))

    def add(self):
        if request.method == 'POST':
            a = request.form['a']
            b = request.form['b']
            return '{} + {} = {}'.format(a, b, int(a) + int(b))
        else:
            a = request.args.get('a')
            b = request.args.get('b')
            return '{} + {} = {}'.format(a, b, int(a) + int(b))

homeController = HomeController()