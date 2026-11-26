# BreatheEasy — Air Quality Monitoring

A Class 12 Informatics Practices project: a friendly dashboard for checking local air quality.

## Run locally

1. Install Python 3.9 or later.
2. In this folder, run `python -m pip install -r requirements.txt`.
3. Run `python app.py`.
4. Open http://127.0.0.1:5000 and choose **Use my location**, or search for a city.

## Share the live website

1. Open **Settings → Pages** in this repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select **main** and **/(root)**, then save.
4. GitHub will show the website link in the Pages section. The root page opens the dashboard in `static/index.html`.

When the hosted page is used, the browser requests AQI data directly from Open-Meteo. If someone chooses **Use my location**, their coordinates are sent to Open-Meteo for that request. BreatheEasy does not save location history, and no API key is required.

## What it shows

- US AQI, a plain-language category, and a friendly health tip
- PM2.5, PM10, ozone, nitrogen dioxide, carbon monoxide, and sulphur dioxide
- A short recent trend and an AQI guide
- An automatic check for updates every 60 seconds

The provider's data may update less often than the dashboard checks, so the AQI can stay the same between updates.

## Air quality guide

The US AQI ranges from 0 to 500: **Good** (0–50), **Moderate** (51–100), **Unhealthy for sensitive groups** (101–150), **Unhealthy** (151–200), **Very unhealthy** (201–300), and **Hazardous** (301+). These are categories for explaining the reading, not medical advice.

PM2.5 and PM10 are tiny airborne particles. Ozone (O3) can form near the ground when other pollutants react in sunlight. Nitrogen dioxide is commonly linked to fuel burning and traffic. Carbon monoxide and sulphur dioxide are gases associated with combustion and industry.

## Project tools and learning goals

- Python and Flask serve the local version and its AQI endpoint.
- HTML, CSS, and JavaScript make the dashboard and request browser location permission.
- Open-Meteo Air Quality API supplies the readings.
- The project demonstrates API use, data presentation, charts, and privacy-aware location handling.

Air-quality values are model estimates and can differ from nearby monitoring stations. Do not use this educational project as emergency or medical advice.

## License

MIT License. See [LICENSE](LICENSE).
