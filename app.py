from fastapi import FastAPI
import requests
import datetime

app = FastAPI()

@app.get("/googleapi/{parameter}")
def example(parameter: str):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0',}

    response = requests.get(parameter, headers=headers)
    return {
        "Url": response.url,
    }

@app.get("/")
def main():
    return {
        "message": "No API exist"
    }