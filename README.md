# Document Automation

A Python project that generates professional PDF reports with data tables and charts using ReportLab.

## Features

- 📊 Generate PDF reports with formatted tables
- 📈 Create bar charts from data
- 🎨 Professional styling with colors and formatting
- 📄 A4 page size support

## Requirements

- Python >= 3.13
- reportlab >= 4.4.10

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Walaa-Volidis/document-automation.git
cd document-automation
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install reportlab
```

Or using pyproject.toml:
```bash
pip install -e .
```

## Usage

Run the script to generate a PDF report:
```bash
python main.py
```

This will create a file named `report.pdf` in the current directory.

## Output

The generated PDF includes:
- **Title**: "Data Analytics Snapshot"
- **Data Table**: Product information with quantities, prices, and totals
- **Bar Chart**: Visual representation of product quantities