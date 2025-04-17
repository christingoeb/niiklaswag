from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])


@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hallo von Flask!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
