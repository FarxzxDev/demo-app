from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Azure GitHub Challenge: Success!</h1><p>Deployed via GitHub Actions.</p>"

if __name__ == "__main__":
    app.run()
