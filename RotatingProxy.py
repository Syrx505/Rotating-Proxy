import requests
import random

# Her seferinde farklı session_number = farklı IP
payload = {
    'api_key': 'YOUR API',
    'url': 'https://urwebsite.com/', <type here which website u want to do proxy
    'country_code': 'be',
    'device_type': 'desktop',
    'max_cost': '1000',
    'session_number': str(random.randint(100000, 999999))  # rastgele oturum → IP değişir
}

r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)
