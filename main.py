from pyrogram import Client, filters
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

# آیدی عددی کاربرانی که باید پیامشون ذخیره بشه
target_user_ids = 1992411831  # ← جایگزین کن

app = Client("bot", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.private)
async def save_user_message(client, message):
    sender_id = message.from_user.id

    if sender_id in target_user_ids:
        with open("saved_messages.txt", "a", encoding="utf-8") as file:
            file.write(f"[{sender_id}] {message.text or '[non-text message]'}\n")
        print(f"Saved message from {sender_id}")


app.run()
