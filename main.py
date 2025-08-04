from pyrogram import Client, filters
import os

api_id = 11991770
api_hash = "e0e93d0f4ff01ceed8006d7a0664848b"

target_user_ids = [1992411831]

channel_username = "@jvjgjvju"  # یوزرنیم کانالت رو اینجا بزن

app = Client("logger_bot", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.private)
async def handler(client, message):
    sender_id = message.from_user.id
    if sender_id in target_user_ids:
        text = message.text or "[non-text message]"
        await app.send_message(channel_username, f"پیام از {sender_id}:\n\n{text}")


app.run()
