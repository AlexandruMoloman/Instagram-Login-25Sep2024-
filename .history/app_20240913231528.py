from flask import Flask

app=Flask(name)

@app.route('/')
def home():
    returnt "WELCOME ALEX!"


if name=='main':
    app.run(debug=True)