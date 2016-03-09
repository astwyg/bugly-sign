from flask import Flask, render_template
app = Flask(__name__, static_folder='front')

@app.route('/')
def hello_world():
    return render_template('index.html', debugMode=True)

if __name__ == '__main__':
    app.run()