# Python CSV Cleaner

A Python automation tool that analyzes CSV files, detects data quality issues, validates email addresses, and generates cleaning reports.

## Features

- Accepts custom CSV file paths
- Detects incomplete records
- Identifies malformed rows
- Performs basic email validation
- Detects duplicate email addresses
- Calculates data quality percentages
- Generates text reports
- Maintains application logs
- Handles empty and missing CSV files

## Technologies Used

- Python
- CSV module
- Logging module
- Datetime module

## Project Structure

```text
CSV_Cleaner/
├── main.py
├── customers.csv
├── employees.csv
├── cleaner.log
├── reports/
│   └── cleaning_report.txt
├── output/
└── samples/
    ├── sample_input.csv
    └── sample_output.csv
```

## How to Run

1. Install Python 3.
2. Open the project folder in your terminal.
3. Run:

```bash
python main.py
```

4. Enter the path to your CSV file when prompted.
5. View the generated report inside the `reports` folder.

## Sample Results

The application reports:

- Total records
- Complete and incomplete records
- Malformed rows
- Valid and invalid emails
- Duplicate and unique emails
- Data quality percentages
- Processing status

## Limitations

- Email validation uses basic checks, not full email-standard validation.
- The sample cleaned CSV is provided as a demonstration; automatic cleaned CSV export is not yet implemented.

## Project Purpose

This project demonstrates practical Python automation, CSV processing, data validation, error handling, and reporting.
