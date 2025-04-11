from flask import Flask, jsonify, request
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return "Date Time live"

@app.route('/datetime', methods=['GET'])
def get_datetime():
    try:
        # Timezone handling
        tz = request.args.get('timezone', 'Europe/Berlin')
        zone = ZoneInfo(tz)
        
        return jsonify({
            "utc_time": datetime.utcnow().isoformat() + "Z",
            "requested_timezone": {
                "time": datetime.now(zone).strftime("%Y-%m-%d %H:%M:%S"),
                "timezone": str(zone)
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run()
