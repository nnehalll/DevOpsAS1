from flask import Flask

app = Flask(__name__)

@app.route('/login')
def hello():
    return "New login are not allowed"

@app.route('/register')
def bello():
    return "we  will have a 30 min break"

@app.route('/logout')
def test():
    return "will logout at 6.30"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)