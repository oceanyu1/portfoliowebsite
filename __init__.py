from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

@app.route("/")
def aboutme():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)