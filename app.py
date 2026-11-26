"""BreatheEasy: a student-friendly air quality dashboard."""

from flask import Flask, jsonify, request, send_from_directory
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import os

app = Flask(__name__, static_folder="static")


def fetch_json(url):
    req = Request(url, headers={"User-Agent": "BreatheEasyClassProject/1.0"})
    with urlopen(req, timeout=12) as response:
        return json.loads(response.read().decode("utf-8"))


@app.get("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/air-quality")
def air_quality():
    try:
        lat = float(request.args["lat"])
        lon = float(request.args["lon"])
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            return jsonify(error="Those coordinates don't look valid."), 400

        params = urlencode({
            "latitude": lat,
            "longitude": lon,
            "current": "us_aqi,european_aqi,pm2_5,pm10,nitrogen_dioxide,ozone,carbon_monoxide,sulphur_dioxide",
            "timezone": "auto",
        })
        data = fetch_json("https://air-quality-api.open-meteo.com/v1/air-quality?" + params)
        return jsonify(data)
    except (KeyError, ValueError):
        return jsonify(error="Please provide a valid latitude and longitude."), 400
    except HTTPError as exc:
        return jsonify(error=f"The air-quality service returned an error ({exc.code}). Try again shortly."), 502
    except (URLError, TimeoutError, json.JSONDecodeError):
        return jsonify(error="I couldn't reach the air-quality service. Check your connection and try again."), 502


if __name__ == "__main__":
    app.run(debug=False, port=int(os.environ.get("PORT", "5000")))
