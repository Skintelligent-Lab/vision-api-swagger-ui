import logging
from os import path
from flask import Flask, request, url_for, send_from_directory, render_template

ROOT_REPO_DIR = path.dirname(__file__)

# logging
LOG_FORMAT = '%(levelname)s:%(module)s:%(threadName)s [%(asctime)s] - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# api config
app = Flask(
    __name__,
    template_folder=ROOT_REPO_DIR,
    static_folder=path.join(ROOT_REPO_DIR, 'static')
)

@app.route('/')
def apidocs_index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
