from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://moloman:Moloman1994@localhost/flask_app'
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "About you do!"

@app.route('/add_user',methods=['POST'] )
def add_user():
    username=request.form['username']
    email=request.form['email']

    new_user=User(username=username, email=email)

    db.session.add(new_user)
    db.session.commit()

    return f"User {username} added successfully!"

@app.route('/user/<username>')
def user_profile(username):
    return f"Hi, {username}!"



@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return f"Hello, {username}!"




if __name__ == '__main__':
    app.run(debug=True)
