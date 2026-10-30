from flask import Flask, render_template
from fetch import fetch_status

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
   hosts = fetch_status()
   return render_template("index.html", hosts = hosts)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
