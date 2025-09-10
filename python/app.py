from flask import Flask

app = Flask(__name__)

@app.route("/")
abhi='ASIAYYMYGL3JBXTDTJ4M'
def home():
    return "Hello from CI Pipeline with Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
