from flask import Flask, render_templates, redirect, url_for

app= Flask(__name__)

@app.route ("/")
def default():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return (render_template("home.html"))


if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
