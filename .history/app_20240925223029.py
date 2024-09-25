from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Конфигурация для Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'  # Например, smtp.gmail.com
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_DEFAULT_SENDER'] = ('Your Name', 'your-email@example.com')

mail = Mail(app)

# Маршрут для отображения формы
@app.route('/')
def index():
    return render_template('form.html')

# Маршрут для обработки отправки формы
@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    try:
        msg = Message(subject, recipients=[email])
        msg.body = message
        mail.send(msg)
        flash('Письмо успешно отправлено!', 'success')
    except Exception as e:
        flash(f'Ошибка при отправке письма: {str(e)}', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
