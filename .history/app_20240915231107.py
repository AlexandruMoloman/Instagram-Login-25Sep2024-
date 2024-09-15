from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    # Обработка изменения пароля
    return render_template('index.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
