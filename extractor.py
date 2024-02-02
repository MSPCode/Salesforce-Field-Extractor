# Import required modules
from datetime import datetime
import openpyxl
from simple_salesforce import Salesforce
import cred  # Ensure this file exists and contains the credentials


SALESFORCE_API_VERSION = cred.SALESFORCE_API_VERSION

def get_salesforce_connection():
    """Establishes a connection to Salesforce using credentials from the cred.py file."""
    username = cred.SALESFORCE_USERNAME
    password = cred.SALESFORCE_PASSWORD
    domain = 'test' if cred.SALESFORCE_SANDBOX else None
    return Salesforce(username=username, password=password, security_token='', domain=domain)

def get_all_objects(sf):
    """Fetches all Salesforce objects, including both standard and custom, excluding objects ending with specific suffixes."""
    url = f'/services/data/v{SALESFORCE_API_VERSION}.0/sobjects/'
    result = sf.query_more(url, True)
    final_list = [
        obj['name'] for obj in result['sobjects']
        if not any(obj['name'].endswith(suffix) for suffix in ('ChangeEvent', 'History', 'Share'))
    ]
    print(f"{len(final_list)} objects will be exported.")
    return final_list

def process_field(field, object_name):
    """Processes individual field metadata and returns a dictionary."""
    data = {
        'OBJECT NAME': object_name,
        'API NAME': field['name'],
        'LABEL': field['label'],
        'TYPE': field['type'].upper(),
        'IS CUSTOM': field['custom'],
        'IS EXTERNAL ID': field.get('externalId', False),
        'IS UNIQUE': field.get('unique', False),
        'IS FORMULA': field.get('calculated', False),
        'IS REQUIRED': not field['nillable'],
        'DEPENDENT PICKLIST': field.get('dependentPicklist', False),
        'LENGTH': field.get('length', None),
        'FORMULA TEXT': field.get('calculatedFormula', None),
        'HELP TEXT': field.get('inlineHelpText', None),
        'PICKLIST VALUES': ', '.join([str(val['label']) for val in field.get('picklistValues', []) if val.get('label') is not None])

    }
    return data

def create_excel_sheet(wb, data, sheet_name):
    """Creates an Excel sheet with specified data, ensuring the sheet name does not exceed 30 characters."""
    # Truncate sheet_name to 30 characters to comply with Excel limitations
    sheet_name = sheet_name[:29]

    ws = wb.create_sheet(title=sheet_name)
    if data:
        ws.append(list(data[0].keys()))  # Column headers
        for row in data:
            ws.append(list(row.values()))

def get_object_fields(sf, object_list, org_name):
    """Exports object fields into an Excel workbook with separate sheets per object."""
    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove the default sheet

    for obj in object_list:
        print(f"Exporting {obj}")
        obj_describe_url = f'/services/data/v{SALESFORCE_API_VERSION}.0/sobjects/{obj}/describe'
        metadata = sf.query_more(obj_describe_url, True)
        data = [process_field(field, obj) for field in metadata['fields']]
        create_excel_sheet(wb, data, obj.lower())

    save_workbook(wb, org_name)

def save_workbook(wb, org_name):
    """Saves the workbook to a file with a timestamp."""
    filename = f"{org_name}_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
    wb.save(filename)
    print(f"Exported to {filename}")

if __name__ == "__main__":
    sf = get_salesforce_connection()
    object_list = get_all_objects(sf) #use this to extract all objects. **THIS MAY NOT WORK IF YOU HAVE LARGE ORG**
    #object_list = ['Account', 'Case', 'Main__c'] #use this if you want to extract specific objects
    get_object_fields(sf, object_list, 'example_org')
