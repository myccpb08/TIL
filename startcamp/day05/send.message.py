import os
import requests
chat_id = os.getenv('CHAT_ID')
token = os.getenv('TELEGRAM_BOT_TOKEN')

text = '안녕'
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=71586203{chat_id}&text={text}')


