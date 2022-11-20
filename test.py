import pandas as pd
from sqlalchemy import create_engine

engine=create_engine("postgresql://postgres:password123@localhost/exam",
                     echo=True)

df = pd.read_sql_query("SELECT * FROM application_data", engine)
engine.dispose()

df.to_csv("output.csv", index=False)