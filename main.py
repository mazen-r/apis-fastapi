from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth, vote

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi',
        user='postgres', password='admin', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print ("Database connection was successful")
        break

    except Exception as error:
        print ("Connecting to database failed")
        print ("Error: ", error)
        time.sleep(2)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message":"Hello World"}






