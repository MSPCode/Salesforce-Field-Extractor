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
   ```

3. **Create a `cred.py` file in the same directory as the script with your Salesforce API credentials and preferences**:

   ```bash
   # cred.py
   SALESFORCE_USERNAME = 'your_username'
   SALESFORCE_PASSWORD = 'your_password'
   SALESFORCE_SECURITY_TOKEN = 'your_security_token'
   SALESFORCE_SANDBOX = True  # or False
   ```

## Usage

To run the script, navigate to the directory containing the script and execute:

```bash
python extractor.py

The script will connect to Salesforce, retrieve the object list, and for each object, it will fetch and export field details to an Excel file named `<org_name>_export_<current_timestamp>.xlsx`.

## Configuration

Object and Field Selection: By default, the script fetches all objects and their fields. Modify the below section in sscript if you need to specify certain objects.

```bash
object_list = get_all_objects(sf) #use this to extract all objects. **THIS MAY NOT WORK IF YOU HAVE LARGE ORG**
#object_list = ['Account', 'Case', 'Main__c'] #use this if you want to extract specific objects


## Security

Ensure that your **`cred.py`** file is securely stored and not included in version control to prevent unauthorized access to your Salesforce credentials.


## Contributing
Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
