from flask import Flask

# generate instance
app = Flask(__name__)

# endpoint
@app.route("/")
def test():
    return "<h1>It Works!</h1>"

# run app
if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True)
