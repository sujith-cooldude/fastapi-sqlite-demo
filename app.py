from fastapi import FastAPI
from sqlite3 import connect

app = FastAPI()

def execute_query(query, params=None):
    with connect("faker_data.db") as connection:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
    return result

@app.get("/users")
async def fetch_users(limit: int = None):
    query = "SELECT * FROM users"
    params = (limit,) if limit is not None else None

    if limit is not None:
        query += " LIMIT ?"

    result = execute_query(query, params)

    return result