from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/useragent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your Browser is {}</p>'.format(user_agent)

if __name__ == '__main__':
    app.run(debug=True)