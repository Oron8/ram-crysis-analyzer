
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine
from . import models
from .api import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='RAM Crysis Analyzer API')
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(api_router, prefix='/api')

@app.get('/')
def root():
    return {'ok': True}
