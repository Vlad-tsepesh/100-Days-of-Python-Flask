from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    # return render_template("index.html", content=[1,2])

@app.route("/<name>")
def user(name):
    # return f"Hello {name}!"
    # return render_template("index.html", content=name)
    return render_template("index.html", content=[1, 2, 3])

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__=="__main__":
    app.run(debug=True)