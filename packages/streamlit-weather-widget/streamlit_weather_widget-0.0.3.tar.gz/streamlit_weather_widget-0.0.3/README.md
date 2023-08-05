# Streamlit Weather Component

A weather component which can be integrated into streamlit Apps.
#### Overview

The Component is made out of a [Open Weather API](https://openweathermap.org/api) and [react-open-weather](https://github.com/farahat80/react-open-weather)

### Requirements
create a `.streamlit/secrets.toml` file in the root folder and set
```
OPEN_WEATHER_KEY = 'YOUR_KEY_HERE' 
```
Upgrade your pip version to latest
`python -m pip install --upgrade pip`
#### Project Docker Deployment

```
docker-compose build
docker-compose up
or in one line `$ docker compose up --build`
# The App is available at http://localhost:8501/
```


#### Required only for Local Setup

```
# Requirments
Python 3.7.1rc2
node v16.14.0.
```

Run it locally locally

```bash
$ python -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit
$ streamlit run streamlit-weather-widget/__init__.py
```

Our React App

```bash
# The whole react app exists in frontend folder
cd streamlit-weather-widget/frontend
npm install
npm run start
```
