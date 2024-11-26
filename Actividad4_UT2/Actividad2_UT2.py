from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify(message="La aplicación está en funcionamiento.")

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
