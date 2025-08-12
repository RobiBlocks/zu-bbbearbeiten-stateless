import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

# Hier wird definiert, auf welche URLs die Applikation reagiert
@app.route("/")
def index():
    todos = helper.get_all()
    return render_template('index.html', todos=todos)

# Hier findet die Ver-BBB-isierung statt
# Hier werden die Daten gespeichert
@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")
    helper.add(title)
    return redirect(url_for("index"))

# Hier werden die Daten an die index.html übergeben
@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))