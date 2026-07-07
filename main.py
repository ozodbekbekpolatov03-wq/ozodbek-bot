from telethon import TelegramClient, events
import asyncio
import time
import threading
from flask import Flask
import os

# --- FLASK SERVER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot tirik!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- BOT QISMI ---
api_id = 35332964
api_hash = "c36507141f58f035186d724e934fba4a"
last_replied = {}
LIMIT_24H = 24 * 60 * 60

client = TelegramClient('ozodbek_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private: # userbot bo'lgani uchun o'zimizga kelgan xabarlarga qaraymiz
        user_id = event.sender_id
        current_time = time.time()
        
        if user_id in last_replied:
            if current_time - last_replied[user_id] < LIMIT_24H:
                return

        sender = await event.get_sender()
        first_name = sender.first_name if sender and sender.first_name else "Do'stim"
        
        reply_text = f"Assalomu alaykum, {first_name}! 😊\n\nMen Ozodbekning yordamchisiman. Ozodbek hozirda biroz band. Xabaringizni qoldiring, u bo'shashi bilan sizga javob beradi! 🤝"
        
        try:
            await asyncio.sleep(1)
            await event.reply(reply_text)
            last_replied[user_id] = current_time
        except Exception as e:
            print(f"Xato: {e}")

async def start_bot():
    # Flaskni bu yerda emas, tashqarida boshlash ma'qul
    await client.start()
    print("🚀 Bot ishga tushdi!")
    await client.run_until_disconnected()

if __name__ == "__main__": # MANA SHU YERDA XATO EDI
    # Flask serverni alohida oqimda ishga tushiramiz
    t = threading.Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    # Botni ishga tushiramiz
    asyncio.run(start_bot())
