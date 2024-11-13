#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
import mysql.connector

app = FastAPI()
DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "azt6gn"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

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

