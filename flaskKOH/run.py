from os import name
from flask import Flask
from flask import request, redirect, url_for, render_template, flash, session
app = Flask(__name__)

@app.route('/')
def show_index():
    values = {"val1":100, "val2":200}
    return render_template('index.html', values = values)

@app.route('/good')
def good():
    name = "Good"
    return name

if __name__ == "__main__":
    app.run(debug=True)

