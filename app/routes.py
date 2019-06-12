from flask import Blueprint
# from controllers.HomeController import HomeController
from app.controllers.HomeController import homeController
routes = Blueprint("routes", __name__)

@routes.route('/', methods=['GET'])
def index():
    return homeController.index()

# Variable rules
@routes.route('/user/<name>/<int:age>/<float:score>')
def hello_user(name, age, score):
    return homeController.hello_user(name, age, score)

@routes.route('/admin')
def hello_admin():
    return homeController.hello_admin()

@routes.route('/person/<name>')
def hello_person(name):
    return homeController.hello_person(name)

@routes.route('/add', methods = ['POST', 'GET'])
def add():
    return homeController.add()