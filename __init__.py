from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route("/")
def about():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/thankyou")
def thank_you():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)