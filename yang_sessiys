
from telethon import TelegramClient, events
import asyncio
import time

# Sening ma'lumotlaring
api_id = 35332964
api_hash = "c36507141f58f035186d724e934fba4a"

# Foydalanuvchilarni vaqtini saqlash uchun lug'at {user_id: oxirgi_vaqt}
last_replied = {}

# 24 soat sekundlarda (24 * 60 * 60)
LIMIT_24H = 86400

# Sessiya fayli nomi
client = TelegramClient('ozodbek_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # Faqat shaxsiy xabarlarga javob beradi (Guruhlarda ishlamaydi)
    if event.is_private:
        user_id = event.sender_id
        current_time = time.time()
        
        # O'zingga o'zing yozsang javob bermaydi
        if event.out:
            return

        # 24 soatlik tekshiruv mantiqi
        if user_id in last_replied:
            last_time = last_replied[user_id]
            # Agar oxirgi javobdan beri 24 soat o'tmagan bo'lsa
            if current_time - last_time < LIMIT_24H:
                print(f"⏩ Foydalanuvchi {user_id} ga hali 24 soat bo'lmadi.")
                return

        # Agar foydalanuvchi yangi bo'lsa yoki 24 soat o'tgan bo'lsa
        sender = await event.get_sender()
        first_name = sender.first_name if sender.first_name else "Do'stim"
        
        reply_text = (
            f"Assalomu alaykum, {first_name}! 😊\n\n"
            "Men Ozodbekning avtomatik yordamchisiman. "
            "Ozodbek hozirda biroz band bo'lishi mumkin. "
            "Xabaringizni qoldiring, u bo'shashi bilan sizga albatta javob beradi. 🤝"
        )
        
        try:
            await asyncio.sleep(1) # Tabiiyroq chiqishi uchun 1 sekund kutish
            await event.reply(reply_text)
            
            # Javob berilgan vaqtni saqlab qo'yamiz
            last_replied[user_id] = current_time
            print(f"✅ {first_name}ga yangi javob yuborildi.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")

async def main():
    # Botni ishga tushirish
    await client.start()
    print("🚀 Userbot ishga tushdi! Endi u 24 soatda bir marta javob beradi.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot to'xtatildi.")
