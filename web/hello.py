from flask import Flask
app = Flask(__name__)


@app.route('/helloget',methods=['GET'])
def hello_world_get():
    return 'GET Hello Flask!'

@app.route('/hellopost',methods=['POST'])
def hello_world_post():
    return 'POST Hello Flask!'


if __name__ == '__main__':
    app.run()