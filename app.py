import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import plotly.express as px
import numpy as np



SERVICE_ACCOUNT_FILE = 'google project api json file location'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = 'spreadsheet end point'
# service = build('sheets', 'v4', credentials=creds)
# spreadsheet = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID).execute()

# sheets = spreadsheet.get('sheets', [])
def fetch_sheet_data():
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID).execute()
    sheets = spreadsheet.get('sheets', [])

    for sheet in sheets:
        title = sheet.get('properties', {}).get('title')
        range = f'{title}'
        result = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range).execute()
        values = result.get('values', {})

        if values:
            df = pd.DataFrame(values)
            df.columns = df.iloc[0]
            df = df[1:]
            return df
    return pd.DataFrame()


app = Flask(__name__)
CORS(app)


@app.route('/get-csv-row-count', methods=['GET'])
def get_csv_row_count():
    # df = pd.read_csv('sample.csv')  # Replace with your CSV file path
    df = fetch_sheet_data()
    row_count = df.shape[0]
    print(row_count)
    return jsonify({'row_count': row_count})








# Run the Flask application
if __name__ == '__main__':
    app.run(port=5000)






