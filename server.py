from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123456'



@app.route('/')
def index():
    if "visit" not in session:
        session["visit"] = 0
    session["visit"] += 1
    return render_template("index.html")

@app.route('/add_visit')
def add_visit():
    if "visit" not in session:
        session["visit"] = 0
    session["visit"] += 1
    return redirect ("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect ("/")



if __name__ == "__main__":
    app.run(debug=True)