# Overview

A Python API via Flask for [erik-web-app](https://github.com/normalone7/erik-web-app).

# Deployment

The Vue app auto-deploys to Heroku on pushes to `main`.

# Running Locally

Install the dependencies

```
pip install -r requirements.txt
```

Run the Flask app

```
python app.py
```

or

```
python3 app.py
```

# Docker setup

I have also used Docker to deploy locally via my home server. I keep the Docker setup for future uses (e.g. I have had a frontend proxy for secure requests to the backend, but I either have to write something custom to auto-deploy to my home Synology server or pay for a hosting service that supports Docker and docker-compose.) One day!

Backend Python Flask image build:

```
docker build --tag normalone7/erik-web-app-python api-server/.
```
