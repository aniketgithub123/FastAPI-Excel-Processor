# main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn
import os

app = FastAPI()

# Allow CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Constants
EXCEL_PATH = os.path.join("Data", "capbudg.xls")

# Load Excel file on startup
try:
    excel_file = pd.ExcelFile(EXCEL_PATH, engine="xlrd")
except FileNotFoundError:
    raise FileNotFoundError(f"Excel file not found at path: {EXCEL_PATH}")
except Exception as e:
    raise RuntimeError(f"Error loading Excel file: {e}")

@app.get("/list_tables")
def list_tables():
    """List all sheet names (tables) in the Excel file."""
    return {"tables": excel_file.sheet_names}

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    """Return the row names (first column values) of a given table."""
    if table_name not in excel_file.sheet_names:
        raise HTTPException(status_code=404, detail="Table not found")

    df = pd.read_excel(excel_file, sheet_name=table_name, engine="xlrd")
    row_names = df.iloc[:, 0].dropna().astype(str).tolist()
    return {"table_name": table_name, "row_names": row_names}

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    """Return the sum of numerical values in the specified row of the table."""
    if table_name not in excel_file.sheet_names:
        raise HTTPException(status_code=404, detail="Table not found")

    df = pd.read_excel(excel_file, sheet_name=table_name, engine="xlrd")
    df = df.fillna(0)

    matched_row = df[df.iloc[:, 0].astype(str).str.strip() == row_name.strip()]
    if matched_row.empty:
        raise HTTPException(status_code=404, detail="Row not found")

    # Sum all numeric values (ignore strings)
    numeric_sum = matched_row.iloc[:, 1:].select_dtypes(include='number').sum(axis=1).values[0]
    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": round(float(numeric_sum), 2)
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9090, reload=True)
