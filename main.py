from fastapi import FastAPI
import requests
from fastapi import Request
app = FastAPI() 




@app.route('/googleapi/{full_path:path}')
def googleapi(full_path: str):
    
    return {"path": full_path}

# async def googleapi(name):


@app.get('/{full_path:path}')
def pred_image(full_path: str):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0',}
    response = requests.get(full_path, headers=headers)
    return response.url