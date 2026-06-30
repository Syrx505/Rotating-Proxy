import requests
import random
import time

for i in range(5):  # 5 farklı istek gönder
    payload = {
        'api_key': 'YOUR API',
        'url': 'https://httpbin.org/ip',
        'session_number': str(random.randint(1000, 999999))
    }
    response = requests.get('https://api.scraperapi.com/', params=payload)
    print(f"Test {i+1} IP:", response.text
    time.sleep(2)  
