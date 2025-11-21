from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Student App!"

if __name__ == '__main__':
    # Use debug=False in production
    app.run(host='0.0.0.0', port=5000, debug=True)
