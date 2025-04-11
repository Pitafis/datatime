from flask import Flask, jsonify, request
from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

app = Flask(__name__)

@app.route('/datetime', methods=['GET'])
def get_datetime():
    # Get local date and time (no timezone)
    local_now = datetime.now()
    local_datetime = local_now.strftime("%Y-%m-%d %H:%M:%S")

    # Get timezone-aware date and time (if requested)
    timezone = request.args.get('timezone', 'Europe/Berlin')  # Default: Berlin
    timezone_data = None

    try:
        tz = ZoneInfo(timezone)
        tz_now = datetime.now(tz)
        tz_datetime = tz_now.strftime("%Y-%m-%d %H:%M:%S %Z")
        timezone_data = {
            "date_and_time": tz_datetime,
            "timezone": str(tz)
        }
    except Exception as e:
        return jsonify({"error": "Invalid timezone"}), 400

    response = {
        "local_date_and_time": local_datetime,
        "timezone_date_and_time": timezone_data
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
