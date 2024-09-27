from datetime import datetime
from flask import Flask
import pytz
#Emos Ker ck3189
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def time():
    tz = pytz.timezone("America/New_York")
    res = "The current date and time is " + str(datetime.now(pytz.utc).astimezone(tz).strftime("%m-%d-%y %H:%M") + " in New York")
    return res

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
