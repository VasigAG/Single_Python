from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"  # Simple string first

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)