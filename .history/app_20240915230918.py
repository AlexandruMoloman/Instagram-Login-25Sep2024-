from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    # Логика для изменения пароля и другой обработки
    # Пример: проверить и обновить пароль в базе данных

    # Перенаправление на страницу с успешным сообщением (или обновление текущей страницы с использованием JavaScript)
    return render_template('index.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
