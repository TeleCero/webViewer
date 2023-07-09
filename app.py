from flask import Flask, render_template, send_from_directory
import os

UPLOAD_PATH = "./upload"
VALID_FILES = ["mp4", "mov"]

app = Flask(__name__)


@app.route('/get_file/<path>')
def get_file(path: str):
  return send_from_directory(UPLOAD_PATH, path)


@app.route('/')
def index():
  fi = os.listdir(UPLOAD_PATH)
  files = [file for file in fi if file.split(".")[-1] in VALID_FILES]
  return render_template('index.html', files)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=89, debug=True)
