from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Конфигурация подключения к MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/flaskapp'
db = SQLAlchemy(app)

# Модель для таблицы пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def home():
    return "Hello, Flask with MySQL!"

if __name__ == '__main__':
    db.create_all()  # Создание таблиц в базе данных
    app.run(debug=True)
