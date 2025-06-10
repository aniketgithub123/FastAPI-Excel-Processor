# 📊 FastAPI Excel Processor

A lightweight and modular FastAPI application to process and query Excel data using **FastAPI**, **Pandas**, and **xlrd**.

---

## 📦 Project Deliverables

- ✅ **GitHub Repository** with clean and well-documented code.
- ✅ `README.md` with setup and usage instructions.
- ✅ **Postman Collection** for testing API endpoints.
- ✅ **Well-structured API** for Excel table inspection and processing.

---

## 🚀 Local Testing

⚙️ Run locally and test via Postman: `http://localhost:9090`  
📁 Use `FastAPI-Excel-Processor.postman_collection.json` for quick testing.

---

## 🖥️ Setup Instructions

### 📌 Install Dependencies

```bash
pip install fastapi uvicorn pandas xlrd
```

### 📌 Run the FastAPI Server
```bash
uvicorn main:app --reload --port 9090
```
---
### 🗃️ Project Structure
```
FastAPI-Excel-Processor/
|
├── Data/
│   └── capbudg.xls                            # Excel file to be processed
├── main.py                                    # FastAPI application
├── FastAPI-Excel-Processor.postman_collection.json  # Postman collection
└── README.md                                  # Project documentation
```
---

### 🌐 API Endpoints
📁 `/list_tables`
| Method | Endpoint       | Description                     |
| ------ | -------------- | ------------------------------- |
| GET    | `/list_tables` | Lists all available sheet names |

**Example Response:**
```bash
{
  "tables": ["CapBudgWS"]
}
```
📁 `/get_table_details?table_name=CapBudgWS`
| Method | Endpoint             | Description                      |
| ------ | -------------------- | -------------------------------- |
| GET    | `/get_table_details` | Lists all first-column row names |

**Example Response:**
```bash
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
```
📁 `/row_sum?table_name=CapBudgWS&row_name=Tax Credit (if any )=`
| Method | Endpoint   | Description                            |
| ------ | ---------- | -------------------------------------- |
| GET    | `/row_sum` | Returns sum of numeric values in a row |

**Example Response:**
```bash
{
  "table_name": "CapBudgWS",
  "row_name": "Tax Credit (if any )=",
  "sum": 0.4
}
```
---
## 🧪 How to Test the App
### ✅ Postman Testing
1. Open Postman. <br>
2. Import `FastAPI-Excel-Processor.postman_collection.json.` <br>
3. Set base URL as `http://localhost:9090.` <br>
4. Test these endpoints: <br>
  - `/list_tables`
  - `/get_table_details?table_name=CapBudgWS`
  - `/row_sum?table_name=CapBudgWS&row_name=Tax Credit (if any )=`


### ✅ Browser Testing
Open these URLs in browser to test GET endpoints directly.

---
## 💡 Developer Insights
### 🔧 Potential Improvements
- Add support for .xlsx via openpyxl
- Add file upload via POST endpoint
- Build a basic UI for selecting files, sheets, and rows
- Implement caching for performance
- Add authentication for secure access
- Optionally support currency/unit symbols in sums

### ⚠️ Known Limitations
- Only supports .xls files
- Empty Excel files may throw errors
- Merged cells/formulas not handled
- Misspelled sheet or row names trigger generic errors
- Rows with no numbers return sum = 0 (can be unclear)
---
## 📚 Technologies Used
- ⚡ **FastAPI**
- 📘 **Pandas**
- 📄 **xlrd**
- 🧪 **Postman**
- 🐍 **Python**


 > 👨‍💻 Built with ❤️ by Aniket Kadam
