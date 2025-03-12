from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

# Load stock data from JSON file
with open("./stocks.json") as f:
    stock_data = json.load(f)

class StockRequest(BaseModel):
    symbol: str

@app.get("/")
def home():
    return {"message": "FastAPI Microservice with CI/CD"}

@app.get("/stocks/")
def get_all_stocks():
    return stock_data["stocks"]

@app.post("/stock-price/")
def get_stock_price(request: StockRequest):
    symbol = request.symbol.upper()
    
    # Check if stock symbol exists in JSON data
    if symbol in stock_data["stocks"]:
        return {"symbol": symbol, **stock_data["stocks"][symbol]}
    else:
        raise HTTPException(status_code=404, detail="Stock not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
