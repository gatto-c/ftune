import flask
import time

app = flask.Flask(__name__, static_folder='../build', static_url_path='/')
app.config["DEBUG"] = True

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/', methods=['GET'])
def index():
    print('>>>>>here<<<<<')
    # return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
    return app.send_static_file('inde1x.html')

@app.route('/time', methods=['GET'])
def get_current_time():
    return {'time': time.time()}

app.run()