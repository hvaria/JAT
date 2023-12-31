from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Load service account credentials
SERVICE_ACCOUNT_FILE = 'jat1-409119-2d497e7fa06e.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of the spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ej8my1niNJCtjTUouGi3L-1iq-jNbTmcUZT_kqK4rNI'
SAMPLE_RANGE_NAME = 'Email Data'  # Adjust the range as needed

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets APIhttps://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project=YOUR_PROJECT_ID

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    for row in values:
        # Print columns A and B, which correspond to indices 0 and 1.
        print(f'{row[0]}, {row[1]}')  # Adjust indices based on your data



