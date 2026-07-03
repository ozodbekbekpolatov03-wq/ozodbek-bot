
from telethon import TelegramClient, events
import asyncio

# Sening ma'lumotlaring
api_id = 35332964
api_hash = "c36507141f58f035186d724e934fba4a"

# Sessiya fayli nomi
client = TelegramClient('ozodbek_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        sender = await event.get_sender()
        first_name = sender.first_name if sender.first_name else "Do'stim"
        
        # O'zingga o'zing yozsang javob bermaydi
        if not event.out:
            reply_text = (
                f"Assalomu alaykum, {first_name}! 😊\n\n"
                "Men Ozodbekning avtomatik yordamchisiman. "
                "Ozodbek hozirda biroz band bo'lishi mumkin. "
                "Xabaringizni qoldiring, u bo'shashi bilan sizga albatta javob beradi. 🤝"
            )
            
            await asyncio.sleep(1) 
            await event.reply(reply_text)
            print(f"✅ {first_name}ga javob yuborildi.")

async def main():
    # Bu yerda telefon raqam va kod so'raladi
    await client.start()
    print("🚀 Bot ishga tushdi!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot to'xtatildi.")
