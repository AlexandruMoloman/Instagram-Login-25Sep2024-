from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    returnt "WELCOME ALEX!"


if __name__=='__main__':
    app.run(debug=True)