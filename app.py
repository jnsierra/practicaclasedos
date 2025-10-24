from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola Mundo en Practica', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
