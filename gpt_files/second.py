from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import requests
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import openai

# Load service account credentials
SERVICE_ACCOUNT_FILE = 'jat1-409119-2d497e7fa06e.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of the spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ej8my1niNJCtjTUouGi3L-1iq-jNbTmcUZT_kqK4rNI'

# SAMPLE_RANGE_NAME = 'Email Data!A1:E'  # Adjust the range as needed

service = build('sheets', 'v4', credentials=creds)



# Call the Sheets API to get values
# Retrieve the sheet metadata to get the titles of each sheet
spreadsheet = service.spreadsheets().get(spreadsheetId=SAMPLE_SPREADSHEET_ID).execute()
sheets = spreadsheet.get('sheets', [])

for sheet in sheets:
    title = sheet.get('properties', {}).get('title')
    range = f'{title}'  # The range is the entire sheet
    result = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range).execute()
    values = result.get('values', [])
    # print(values)



# # Function to interact with OpenAI's GPT
# def ask_openai(prompt):
#     OPENAI_API_KEY = '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'
#     response = requests.post(
#         'https://api.openai.com/v1/engines/davinci/completions',
#         headers={
#             'Authorization': f'Bearer {OPENAI_API_KEY}',
#             'Content-Type': 'application/json'
#         },
#         json={
#             'prompt': prompt,
#             'max_tokens': 50  # Adjust as necessary
#         }
#     )
#     response_json = response.json()
#     print(response_json)

# def generate_text(email_body, max_length=50):
#     prompt = "Email content: " + email_body + "\nwhich is the job psition in this email?"
#     tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#     model = GPT2LMHeadModel.from_pretrained("gpt2")

#     # Preprocess the prompt to take only the first 50 words
#     words = prompt.split()[:50]  # Split the text and take the first 50 words
#     truncated_prompt = ' '.join(words)

#     inputs = tokenizer.encode(truncated_prompt, return_tensors='pt', max_length=1024, truncation=True)
#     # print(f"Sending prompt to model: {prompt}")
#     output = model.generate(inputs, max_length=max_length, num_return_sequences=1)
#     generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
#     print(f"Model generated: {generated_text}")
#     return generated_text


def generate_text_with_gpt3(prompt, max_tokens=100, engine="davinci"):
    openai.api_key = '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'  # Replace with your actual API key

    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
prompt = "Translate the following English text to French: 'Hello, how are you?'"
generated_text = generate_text_with_gpt3(prompt)
print
(generated_text)
exit()
from transformers import pipeline
import re


# def generate_text_with_gpt3(email_body, max_tokens=100, engine="davinci"):
#     openai.api_key = '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'  # Replace with your actual API key
#     truncated_email_body = ' '.join(email_body.split()[:50])
#     prompt=f"Determine from email, which job title was appliaction submitted?\nEmail: {truncated_email_body}"
#     print('Promet:',prompt)
#     try:
#         response = openai.Completion.create(
#             engine=engine,
#             prompt=prompt,
#             max_tokens=max_tokens
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None



def generate_job_title(email_body):
    generator = pipeline('text-generation', model='gpt2')

    # Further truncate the email body to a suitable length
    truncated_email_body = ' '.join(email_body.split()[:50])  # try first 50 words

    # prompt = f"Email: {truncated_email_body}\nExtracted job title:"

    prompt=f"Determine from email, which job title was appliaction submitted?\nEmail: {truncated_email_body}"
    
    # Debugging: Print the length of the tokenized input
    tokenized_input = generator.tokenizer(prompt)
    print(f"Length of tokenized input: {len(tokenized_input['input_ids'])}")

    # Ensure the length is within the model's limits
    if len(tokenized_input['input_ids']) > 1024:
        raise ValueError("Tokenized input is too long for the model.")

    response = generator(prompt, max_length=50, num_return_sequences=1)

    output = response[0]['generated_text'].strip()
    print("GPT RESPONSE ++++>",output)
    return output




def clean_email_body(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove special characters and excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text



#______main______________

email_body_column_index = 2
new_column_index = 3  # Assuming you want to put job titles in the next column

for sheet in sheets:
    title = sheet.get('properties', {}).get('title')
    range = f'{title}'  # The range for the entire sheet
    result = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range).execute()
    values = result.get('values', [])

    if not values:
        continue  # Skip empty sheets

    updated_values = []
    for i, row in enumerate(values):
        if i >= 10:  # Process only the first 20 rows
            break

        email_body = row[email_body_column_index] if len(row) > email_body_column_index else ""
        email_body = clean_email_body(email_body)
        job_title=generate_text_with_gpt3(email_body)
        print(job_title)
        if len(row) > new_column_index:
            row[new_column_index] = job_title  # Update existing row
        else:
            row.append(job_title)  # Append job title to the row
        updated_values.append(row)

    # Update the Google Sheet with new values
    update_range = f'{title}!A1'  # Adjust as per your sheet structure
    body = {'values': updated_values}
    service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=update_range,
        valueInputOption='RAW', body=body).execute()

print("Job titles generated and sheet updated.")