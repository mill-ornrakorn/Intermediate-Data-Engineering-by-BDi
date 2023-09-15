from fastapi import FastAPI, HTTPException, Header
import requests

app = FastAPI(root_path="/books")

mocked_data = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

@app.get("/")
async def read_books(x_api_key: str = Header()):
    if x_api_key:
        response = requests.post("http://auth_service:80/verify", headers={"X-Api-Key": x_api_key})
        if response.status_code == 200:
            return {"data": mocked_data}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        raise HTTPException(status_code=400, detail="No API key provided")
