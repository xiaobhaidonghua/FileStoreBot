from config import settings
import requests

class Telegram_API():
    def __init__(self):
        self.api = f"https://api.telegram.org/bot{settings.BOT_TOKEN}"
    
    def copyMessage(self, chat_id, from_chat_id, message_id):
        url = f"{self.api}/copyMessage"
        data = {
            "chat_id": int(chat_id),
            "from_chat_id": int(from_chat_id),
            "message_id": int(message_id)
        }
        response = requests.post(url, data=data)
        return response.json()['result']['message_id'] if response.status_code == 200 else None