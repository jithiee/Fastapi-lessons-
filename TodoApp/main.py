from fastapi import FastAPI
import models
from database import engine 

# this file for create database connection for Api

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

