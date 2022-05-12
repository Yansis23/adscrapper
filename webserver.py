from flask import Flask
from threading import Thread
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask("")

@app.route("/")
def index():
  return "AD Scraper Is Online - Credits MonkeLord69"

def run():
    app.run(host="0.0.0.0", port=8080)

def start():
    server = Thread(target=run)
    server.start()