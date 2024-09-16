from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройки для базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # Пример с SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Определение модели
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Создание таблиц в контексте приложения
with app.app_context():
    db.create_all()

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)