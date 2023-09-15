from fastapi import FastAPI, HTTPException, Request, Header

app = FastAPI()

@app.post("/verify")
async def verify(x_api_key: str = Header()):
    if not x_api_key:
        raise HTTPException(status_code=400, detail="X-Api-Key header missing")

    if x_api_key == "thisiscool":
        return {"authorized": True}

    raise HTTPException(status_code=401, detail="Unauthorized")
