from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Инициализация приложения и настройка базы данных
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fest_searcher.db?charset=utf8"
app.config["SQLALCHEMY_DATABASE_CHARSET"] = 'utf8'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
CORS(app)

migrate = Migrate(app, db)

# Импорт моделей и функций
from utils import create_user, authenticate_user, create_account, \
    get_user_id, Fest, add_fest, delete_fest_by_name


# Регистрация пользователя
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if create_user(username, password, email):
        return jsonify({"message": "User created"}), 201
    return jsonify({"error": "Failed to create user"}), 400


# Авторизация пользователя
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = authenticate_user(username, password)
    if user:
        return jsonify({"message": "Logged in", "id": user.id}), 200
    return jsonify({"error": "Invalid username or password"}), 401


@app.route("/accounts", methods=["POST"])
def new_account():
    data = request.get_json()
    user_id = data.get("user_id")

    if create_account(user_id):
        return jsonify({"message": "Account created"}), 201
    return jsonify({"error": "Failed to create account"}), 400


@app.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()
    username = data.get('username')
    id = get_user_id(username)

    if id:
        return jsonify({"id": id}), 201
    return jsonify({"error": "Failed to get id"}), 400


@app.route('/fests', methods=["GET"])
def get_all_fests():
    fests = Fest.query.all()
    fest_list = [fest.to_dict() for fest in fests]
    return jsonify(fest_list), 200


@app.route("/addfest", methods=["POST"])
def add_new_fest():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time")
    category_name = data.get("category_name")
    price = data.get("price")
    location = data.get("location")

    if add_fest(name, description, date_time, category_name, price, location):
        return jsonify({"message": "New fest added"}), 201
    return jsonify({"message": "New fest added"}), 202


@app.route("/deletefest", methods=["DELETE"])
def delete_fest():
    data = request.get_json()
    name = data.get("name")

    if delete_fest_by_name(name):
        return jsonify({"message": "Fest deleted"}), 200
    return jsonify({"error": "Failed to delete fest"}), 400


if __name__ == "__main__":
    app.run(debug=True, host='192.168.56.1')
