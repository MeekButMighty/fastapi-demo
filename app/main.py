#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "azt6gn"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; replace "*" with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

@app.get("/genres")
async def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = [dict(zip(headers, result)) for result in results]
        return json_data
    except mysql.connector.Error as e:
        print("MySQL Error:", str(e))
        return {"error": str(e)}
    finally:
        cur.close()

@app.get("/songs")
async def get_songs():
    query = "SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, songs.image, genres.genre FROM songs JOIN genres ON songs.genre = genres.genreid;"  # Complete SQL query here
    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = [dict(zip(headers, result)) for result in results]
        return json_data
    except mysql.connector.Error as e:
        print("MySQL Error:", str(e))
        return {"error": str(e)}
    finally:
        cur.close()


@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "I did my lab! yay!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/square/{c}")
def square(c: int):
    return {"square": c*c}

@app.get("/subtract/{d}/{e}")
def subtract(d: int, e: int):
    return {"difference": d-e}

