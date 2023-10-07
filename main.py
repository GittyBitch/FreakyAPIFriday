import logging
import sys
import argparse

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

CONST_HOST = "0.0.0.0"
CONST_PORT = 8000
CONST_DEFAULT_MSG = "Todo bien"

class Item(BaseModel):
    name: str
    description: str
    price: float
    total_price: Optional[float] = None
    tax: float
    amount: int

app = FastAPI()
app.myItems = []

@app.get("/")
def default() -> str:
    return CONST_DEFAULT_MSG

@app.get("/items")
def read_root() -> List[Item]:
    return app.myItems

@app.get("/clear-items")
def read_root():
    app.myItems = []
    return app.myItems

@app.post("/item")
def post_item(item: Item) -> Item:
    app.myItems.append(item)
    return item

def main(host, port):
    logging.info("Python Version:"+sys.version)
    logging.info("FastAPI Demo:"+app.version)
    import uvicorn
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process host and port.')
    parser.add_argument('--host', type=str, required=False, help='The host IP address.', default=CONST_HOST)
    parser.add_argument('--port', type=int, required=False, help='The port number.',default=CONST_PORT)
    args = parser.parse_args()
    main(args.host, args.port)


