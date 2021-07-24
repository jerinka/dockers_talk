from flask import Flask
app = Flask(__name__)

@app.route('/')
def pong_service():
    return 'Hello, I am pong service!'

@app.route('/pong')
def do_pong():
    return 'Pong'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug = True)
