from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # Используется SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Определение модели User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Создание таблиц
with app.app_context():
    db.create_all()

# Маршрут для главной страницы
@app.route('/')
def home():
    return "Hello, Flask!"

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
