from fastapi import FastAPI
import requests
from fastapi import Request
import urllib.parse
app = FastAPI() 




@app.get('/api/{full_path:path}')
async def pred_image(full_path: str):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0',}
    full_path =urllib.parse.unquote(full_path)
    google = "https://lens.google.com/uploadbyurl?url="
    full_path = google+full_path
    response = requests.get(full_path, headers=headers)
    return response.url


@app.get('/')
def pred():
    return "Test"