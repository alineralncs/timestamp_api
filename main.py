from fastapi import FastAPI

from routers import timestamp_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Timestamp API is running"}


app.include_router(timestamp_router.router)
