from fastapi import FastAPI
from endpoints.endpoints import api_router

app = FastAPI()
app.include_router(api_router)