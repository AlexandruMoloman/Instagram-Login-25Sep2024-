from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://moloman:Moloman1994@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель пользователя (пример)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    
    user = User.query.filter_by(username=username, password=old_password).first()
    if user:
        user.password = new_password
        db.session.commit()
        message = f"Пароль был изменен для аккаунта {username}"
    else:
        message = "Пользователь не найден или старый пароль неверен."
    
    return render_template('index.html', message=message, username=username)

if __name__ == '__main__':
    app.run(debug=True)
