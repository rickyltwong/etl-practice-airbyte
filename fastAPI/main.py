import math
import pandas as pd
from fastapi import FastAPI

def read_data(file_name: str):
    df = pd.read_csv(file_name)
    return df.to_string()

app = FastAPI()
file_name = "Dragon_Ball_Data_Set.csv"
db_data = read_data(file_name)




@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data")
def get_data():
    return db_data 

