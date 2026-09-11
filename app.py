from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv('APP_VERSION', '1.0.0')
ENV = os.getenv('ENVIRONMENT', 'development')

@app.route('/')
def home():
    return jsonify({
        'app': 'CI/CD Demo',
        'version': VERSION,
        'environment': ENV,
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

def add(a, b):
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
