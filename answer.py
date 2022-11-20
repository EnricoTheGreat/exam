from fastapi import FastAPI
from sqlalchemy import create_engine
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel, BaseSettings
import pandas as pd
import psycopg2


class Settings(BaseSettings):
    db_hostname: str = "localhost"
    db_username: str = "postgres"
    db_name: str = "exam"
    db_password: str = "password123"
class Second(BaseModel):
    corporate_key: str

app = FastAPI()

try:
    conn = psycopg2.connect(host="localhost", database="exam", user="postgres", password="password123",
                            cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

#The first API joins the three tables to have a list of the application, IT custodians , Team Members associated to that custodian
# and Managers of that custodian. This shows the relationship between those tables.
@app.get("/first")
def get_password_vault_requests():
    cursor.execute("""SELECT distinct app_name , itcustodian_name , cn member, managers 
    FROM password_vault_requests p
    INNER JOIN application_data a
    ON p."Server" = a.server_name
    INNER JOIN hierarchy_data h
    ON a.itcustodian_name = h.managers""")
    get_inventory = cursor.fetchall()
    return {"data": get_inventory}

#This second API will query the database for the application_data to
#display the related data associated to the corporated key sent out via Postman.
@app.post('/second')
def get_details(payload: Second):
    query = cursor.execute(""" SELECT * FROM  application_data
    WHERE it_custodian_ck = %s """, (payload.corporate_key,))
    second_api = cursor.fetchall()



    return {"data": second_api}






#This third API checks to see whether there is/are existing tables in the database using
#Count(*), this can be use to check if the database is empty or not
@app.get('/check_db')
def check_db():
    cursor.execute (""" SELECT COUNT(*)
  FROM information_schema.tables
 WHERE table_type = 'BASE TABLE'
   AND table_schema = 'public'""")
    db_status = cursor.fetchone()
    print(db_status)
    return {"Database Table Count": db_status}
