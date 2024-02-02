# Salesforce Object and Field Exporter

This Python script connects to Salesforce, retrieves a comprehensive list of Salesforce objects, including both standard and custom objects, and exports detailed information about each object's fields into an Excel file. It filters out objects related to change events, history, or shares by default.

## Features

- Connects to Salesforce using provided API credentials.
- Retrieves and filters Salesforce objects based on predefined criteria.
- Exports details of object fields into an Excel file, with separate sheets for each object.

## Prerequisites

Before running this script, you must have:

- Python 3.x installed.
- `simple_salesforce` Python package installed.
- `openpyxl` Python package installed.

## Installation

1. **Clone or download this repository** to your local machine.

2. **Install the required Python packages** by running:

   ```bash
   pip install simple_salesforce openpyxl
