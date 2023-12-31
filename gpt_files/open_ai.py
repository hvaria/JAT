import requests

def ask_openai(prompt):
    OPENAI_API_KEY = 'your-openai-api-key'
    response = requests.post(
        'https://api.openai.com/v1/engines/gpt-4/completions',
        headers={
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        },
        json={
            'prompt': prompt,
            'max_tokens': 50  # Adjust as necessary
        }
    )
    response_json = response.json()
    return response_json['choices'][0]['text'].strip()
