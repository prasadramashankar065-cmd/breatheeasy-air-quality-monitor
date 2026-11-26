# BreatheEasy — Air Quality Monitoring

A Class 12 Informatics Practices project: a friendly, location-based dashboard for exploring air quality.

## Run locally

1. Install Python 3.9 or later.
2. Open a terminal in this folder and run `python -m pip install -r requirements.txt`.
3. Run `python app.py`.
4. Open `http://127.0.0.1:5000` in a browser and choose **Use my location**. Allow location access when your browser asks.

You can also search for a city to explore the dashboard without using device location.

## Share the live website

This repository includes a GitHub Pages entry point. After the project files are uploaded, open **Settings → Pages**, choose **Deploy from a branch**, select **main** and **/(root)**, then save. GitHub will show the shareable website address in that Pages section. The browser requests AQI and current weather data directly from Open-Meteo. If a visitor chooses **Use my location**, their coordinates are sent to Open-Meteo for those requests; BreatheEasy does not save location history.

## What it shows

- US AQI and a plain-language air-quality category
- PM2.5, PM10, NO₂, O₃, CO, and SO₂
- Current temperature, feels-like temperature, humidity, precipitation, wind speed, direction, and gusts
- A short health suggestion and recent AQI trend
- Automatic refresh every 60 seconds

The refresh checks for newer information every minute. The source may update its underlying air-quality model less often, so the displayed AQI can stay the same between updates. Model estimates are not a substitute for readings from a nearby monitoring station.

## Project tools

- Python and Flask serve the app and retrieve the data.
- HTML, CSS, and JavaScript create the dashboard and request location permission.
- Open-Meteo Air Quality and Weather APIs supply the readings; no API key is needed for this school project.

The browser shares coordinates only after the user allows location access. The dashboard also works with a searched city. The project does not save location history.

## Data and limitations

Air-quality readings come from the [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api), and weather readings come from the [Open-Meteo Weather API](https://open-meteo.com/en/docs). The page checks for updates every 60 seconds, but the provider's underlying models update less often. Values are model estimates and can differ from nearby monitoring stations. Do not use the dashboard as emergency or medical advice.

## Project learning goals

- Request data from a web API and display selected fields.
- Use Python with Flask to provide a simple web service.
- Present information with charts, categories, and clear labels.
- Discuss data quality, location privacy, and the limits of model estimates.

## License

This project is shared under the MIT License. See [LICENSE](LICENSE).
