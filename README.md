📊 FastAPI Excel Processor
📘 Overview
This FastAPI application reads an Excel file (capbudg.xls) and provides API endpoints to:

✅ List all sheet names (considered as tables)

✅ Show all row names (first-column values) from a selected sheet

✅ Calculate the sum of all numerical values in a specified row

📍 Base URL: http://localhost:9090

🚀 Getting Started
1️⃣ Install Dependencies
bash
Copy
Edit
pip install fastapi uvicorn pandas xlrd
2️⃣ Project Structure
css
Copy
Edit
FastAPI-Excel-Processor/
├── Data/
│   └── capbudg.xls
├── main.py
├── FastAPI-Excel-Processor.postman_collection.json
└── README.md
3️⃣ Run the FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload --port 9090
Then open your browser or Postman to test the endpoints.

🔌 API Endpoints
📂 GET /list_tables
Lists all available sheet names in the Excel file.

✅ Example Response
json
Copy
Edit
{
  "tables": ["CapBudgWS"]
}
📂 GET /get_table_details?table_name=CapBudgWS
Returns all first-column values (row names) from the specified sheet.

✅ Example Response
json
Copy
Edit
{
  "table_name": "CapBudgWS",
  "row_names": [
    "Initial Investment=",
    "Opportunity cost (if any)=",
    "Lifetime of the investment",
    "Salvage Value at end of project=",
    "Deprec. method(1:St.line;2:DDB)=",
    "Tax Credit (if any )=",
    "Other invest.(non-depreciable)="
  ]
}
📂 GET /row_sum?table_name=CapBudgWS&row_name=Tax Credit (if any )=
Calculates and returns the sum of all numeric values in the specified row.

✅ Example Response
json
Copy
Edit
{
  "table_name": "CapBudgWS",
  "row_name": "Tax Credit (if any )=",
  "sum": 0.4
}
🧠 Developer Insights
🔧 Potential Improvements
Add support for .xlsx files via openpyxl

Add file upload support via POST endpoint

Add a simple UI for selecting files, sheets, and rows

Implement caching for performance

Add authentication for secure access

Optionally display units (like %) in row sums

⚠️ Known Limitations
Empty Excel files may cause errors

Misspelled sheet or row names cause generic errors

Rows with no numeric values return sum = 0, which may be unclear

Merged cells and Excel formulas aren't explicitly handled

🧪 Testing (Postman)
A Postman collection is included:

📁 FastAPI-Excel-Processor.postman_collection.json

✅ How to Use:
Open Postman

Click Import → File and select the collection file

Set the base URL to: http://localhost:9090

Test the endpoints:

/list_tables

/get_table_details

/row_sum

📚 Technologies Used
⚡ FastAPI

📘 Pandas

📄 xlrd

🧪 Postman

🐍 Python 3

👨‍💻 Author
Aniket Kadam
AI/ML Developer & FastAPI Enthusiast

📫 GitHub | LinkedIn
