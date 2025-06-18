from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# Маппинг между ID и локацией
default_locations = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen"
}

default_ids = {
    "Living Room": "1",
    "Bedroom": "2",
    "Kitchen": "3"
}


@app.route("/temperature/<sensor_id>", methods=["GET"])
def get_temperature_by_id(sensor_id):
    location = request.args.get("location", "")

    # Если location не указан — определяем его по sensor_id
    if not location:
        location = default_locations.get(sensor_id, "Unknown")

    response = {
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "value": round(random.uniform(15.0, 25.0), 2),
        "unit": "C",
        "status": "active",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "location": location,
        "description": "Temperature sensor reading by ID"
    }
    return jsonify(response)


@app.route("/temperature", methods=["GET"])
def get_temperature_by_location():
    location = request.args.get("location", "")
    sensor_id = request.args.get("sensor_id", "")

    # Если sensor_id не указан — определяем его по location
    if not sensor_id:
        sensor_id = default_ids.get(location, "0")

    # Если location не указан — определяем его по sensor_id
    if not location:
        location = default_locations.get(sensor_id, "Unknown")

    response = {
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "value": round(random.uniform(15.0, 25.0), 2),
        "unit": "C",
        "status": "active",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "location": location,
        "description": "Temperature sensor reading by location"
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)