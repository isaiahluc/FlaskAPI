from flask import Flask, jsonify, request
from datetime import datetime
from zoneinfo import ZoneInfo


app = Flask(__name__)

API_TOKEN = "bviurwbrvuijv1256"

def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator


# basic testing
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

# security testing
@app.route('/api/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({"secret": "This is protected info!"})

# new endpoint: lookup current time in a capital
CAPITAL_TIMEZONES = {
    "London":      "Europe/London",
    "New York":    "America/New_York",
    "Tokyo":       "Asia/Tokyo",
    "Sydney":      "Australia/Sydney",
    "Paris":       "Europe/Paris",
    # … add as needed …
}


@app.route('/api/time/<capital>', methods=['GET'])
@token_required
def get_time(capital):
    tz_name = CAPITAL_TIMEZONES.get(capital)
    if not tz_name:
        return jsonify({
            "error": f"Unknown capital '{capital}'.  Available: {list(CAPITAL_TIMEZONES)}"
        }), 404

    # get now in that timezone
    now = datetime.now(ZoneInfo(tz_name))
    # format UTC offset as ±HH:MM
    offset = now.utcoffset()
    total_minutes = offset.total_seconds() // 60
    hours, minutes = divmod(abs(int(total_minutes)), 60)
    sign = "+" if total_minutes >= 0 else "-"
    utc_offset = f"UTC{sign}{hours:02d}:{minutes:02d}"

    return jsonify({
        "capital":      capital,
        "local_time":   now.isoformat(),
        "utc_offset":   utc_offset
    })




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)