#This .py file is for the Task 3 under Handson_05 Step 71 to expose data.json at /post get request
# This is implemented using FASTAPI
#

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn
app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],allow_credentials=True,allow_methods=['GET'],allow_headers=["Content-Type","Authorization"]
)

@app.get("/posts")
def get_posts():
    with open("data.json","r",encoding="utf-8") as file:
        data = json.load(file)
    return data

def main():
    uvicorn.run("app:app",host="127.0.0.1",port=8000,reload=True)

if __name__ == "__main__":
    main()