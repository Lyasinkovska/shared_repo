from flask import Flask, render_template, request

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__,)


@app.route("/354")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
