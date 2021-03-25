from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/layout/')
def layout():
    return render_template('layout.html')

@app.route('/tune1/')
def tune1():
    return render_template('tune1.html')

@app.route('/tune2/')
def tune2():
    return render_template('tune2.html')

@app.route('/tune3/')
def tune3():
    return render_template('tune3.html')

if __name__ == '__main__':
    app.run(debug=True)

