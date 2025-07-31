from telethon.sync import TelegramClient
from sys import argv

API_ID = 123456  # مقدار واقعی
API_HASH = 'your_api_hash'

b = TelegramClient('ok', API_ID, API_HASH).start()

mess = b.get_messages(argv[1], limit=int(argv[2]))
for i in mess[-1].reply_markup.rows:
    for n in i.buttons:
        print(n.text, '=', n.data)
    print()

b.disconnect()
