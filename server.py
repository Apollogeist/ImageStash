from flask import Flask
from flask import request
import IP2Location
import os

database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB3.BIN"), "SHARED_MEMORY")

app = Flask(__name__)


@app.route('/')
def index():
    ip = request.remote_addr
    rec = database.get_all(ip)
    print(f"Access from IP: {ip} | {rec.city}, {rec.region} ({rec.country_short})")
    return "<h1>404 - Not Found</h1>"