from flask import Flask

app = Flask(__name__)

@app.route("/home")

def home():
	return "<h1>test</h1>"

if __name__ == "__main__":
	app.run()