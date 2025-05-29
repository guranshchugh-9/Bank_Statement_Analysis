# 🏦 Bank Statement Analyzer

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Workflow-PDF→Excel→CSV→Visualization-orange" alt="Workflow">
</div>

## 🌟 Overview
A streamlined end-to-end pipeline that converts your PDF bank statement into clean, categorized data and actionable visual insights. Track your income vs. expenses, see category-wise spending breakdowns, and integrate with any backend.

---

## ✨ Key Features

| Feature                               | Description                                                      |
|---------------------------------------|------------------------------------------------------------------|
| **📄 PDF → Excel/CSV Conversion**      | Automatically extracts tables from PDF into Excel & CSV files.  |
| **🧹 Data Cleaning & Formatting**      | Standardizes columns: Date, Narration, Withdrawals, Deposits, Balance. |
| **🗂️ Transaction Categorization**      | Tags each transaction into categories like Groceries, Rent, Utilities. |
| **📊 Financial Summary**               | Computes total income/expenses, average savings, spending trends. |
| **📈 Visualizations**                  | • Pie chart: Expense breakdown by category  
                                         | • Line graph: Monthly income vs. expenses

---

## 🏗️ Project Structure

```
.
├── uploads/                      
│   └── your_bank_statement.pdf      # Place your raw PDF here
├── processed_files/                
│   ├── converted_excel.xlsx         # Output from step 2
│   ├── cleaned_data.csv             # Output from step 3
│   ├── categorized_data.csv         # Output from step 4
│   ├── expenses_by_category_pie.png # Generated pie chart
│   ├── monthly_income_vs_expenses_line.png # Generated line graph
│   ├── 1-main.py                    # Runs the entire pipeline
│   ├── 2-convert_pdf_to_excel.py    # PDF → Excel converter
│   ├── 3-clean_data.py              # Data cleaning & formatting
│   ├── 4-categorize_transactions.py # Transaction categorizer
│   ├── 5-financial_summary.py       # Summarizes income/expenses
│   ├── 6-generate_graphs.py         # Creates pie & line graphs
│   └── 7-backend.py                 # (Optional) Flask/FastAPI integration
└── README.md                        # This file
```

---

## 🛠️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/bank-statement-analyzer.git
   cd bank-statement-analyzer
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

_Recommended packages:_ `pandas`, `matplotlib`, `pdfplumber`, `openpyxl`, `Flask` (or `FastAPI`).

---

## 🚀 Quick Start

1. **Add** your bank statement PDF to the `uploads/` folder.
2. **Run** the main pipeline:
   ```bash
   python processed_files/1-main.py
   ```
3. **Inspect** results in `processed_files/`:
   - `converted_excel.xlsx`
   - `cleaned_data.csv`
   - `categorized_data.csv`
   - `expenses_by_category_pie.png`
   - `monthly_income_vs_expenses_line.png`

---

## 📦 Usage Examples

```python
# In 1-main.py
from convert_pdf_to_excel import convert
from clean_data import clean
from categorize_transactions import categorize
from financial_summary import summarize
from generate_graphs import plot_pie, plot_line

# 1. Convert
excel_path = convert("uploads/your_bank_statement.pdf")

# 2. Clean
csv_path = clean(excel_path)

# 3. Categorize
cat_csv = categorize(csv_path)

# 4. Summarize
summary = summarize(cat_csv)

# 5. Visualize
plot_pie(cat_csv, output="processed_files/expenses_by_category_pie.png")
plot_line(summary, output="processed_files/monthly_income_vs_expenses_line.png")
```

---

## 🧩 Tech Stack

<div align="center">
  <img src="https://img.shields.io/badge/Python-pandas-orange" alt="pandas">
  <img src="https://img.shields.io/badge/Visualization-matplotlib-red" alt="matplotlib">
  <img src="https://img.shields.io/badge/PDF-OCR_pdfplumber-blue" alt="pdfplumber">
  <img src="https://img.shields.io/badge/Web%20API-Flask%2FFastAPI-blue" alt="Flask/FastAPI">
</div>

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch (`git checkout -b feat/your-feature`)  
3. Commit your changes (`git commit -m 'feat: add new feature'`)  
4. Push to the branch (`git push origin feat/your-feature`)  
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

---

<div align="center"> Made with ❤️ by **Your Name** [Report Bug](https://github.com/yourusername/bank-statement-analyzer/issues) · [Request Feature](https://github.com/yourusername/bank-statement-analyzer/discussions) </div> 
```
