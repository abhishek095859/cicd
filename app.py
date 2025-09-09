from flask import Flask

app = Flask(__name__)
token="akjbmpkmcpwj39932i920jj092e22j233jm"

@app.route("/")
def home():
    return "Hello from CI Pipeline with Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
