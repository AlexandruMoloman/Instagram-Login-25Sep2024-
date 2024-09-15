from flask import Flask

app=Flask(__name__)



@app.route('/')
def home():
    return render_tempates('index.html', name="Flask")

@app.route('about')
def about():
    return "About you do!"

@app.route('/user/<username>')
def user_profile(username):
    return "Hi, {username}!"

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return "Hello, {username}!"

if __name__=='__main__':
    app.run(debug=True)