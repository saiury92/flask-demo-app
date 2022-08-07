from flask import Flask
from user.user import user


app = Flask(__name__)
app.register_blueprint(user)

@app.route('/')
def home():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
