import os
import shutil
import logging
from dotenv import load_dotenv
import telebot
import instaloader

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("InstaSaverBot")

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("BOT_TOKEN is not set in environment or .env file!")
    print("\n[ERROR] Iltimos, .env faylida yoki muhitda BOT_TOKEN ni belgilang!\n")

bot = telebot.TeleBot(BOT_TOKEN) if BOT_TOKEN else None

loader = instaloader.Instaloader(
    download_comments=False,
    download_geotags=False,
    download_pictures=False,
    download_video_thumbnails=False,
    save_metadata=False
)

@bot.message_handler(commands=['start', 'help'])
def start_handler(message):
    welcome_text = (
        "🚀 **Assalomu alaykum!**\n\n"
        "**TIJEY Studio** ning Instagram video & reels yuklovchi botiga xush kelibsiz.\n\n"
        "📥 Menga shunchaki Instagram post yoki reels havolasini (linkini) yuboring!"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def download_handler(message):
    url = (message.text or "").strip()

    if "instagram.com" not in url:
        bot.reply_to(message, "⚠️ Iltimos, to'g'ri Instagram havolasini yuboring.")
        return

    try:
        # Extract shortcode from URL
        parts = [p for p in url.split("?")[0].split("/") if p]
        if len(parts) < 2:
            raise IndexError("Invalid URL structure")
        shortcode = parts[-1] if parts[-2] in ["p", "reel", "reels", "tv"] else parts[-1]
    except Exception:
        bot.reply_to(message, "⚠️ Siz yuborgan havola noto'g'ri! Tekshirib qaytadan yuboring.")
        return

    status_msg = bot.send_message(message.chat.id, "⏳ Video yuklab olinmoqda, iltimos kuting...")

    try:
        logger.info(f"Downloading post with shortcode: {shortcode}")
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=shortcode)

        video_file = None
        if os.path.exists(shortcode):
            for file in os.listdir(shortcode):
                if file.endswith(".mp4"):
                    video_file = os.path.join(shortcode, file)
                    break

        if video_file and os.path.exists(video_file):
            bot.edit_message_text("📤 Video yuborilmoqda...", chat_id=message.chat.id, message_id=status_msg.message_id)
            with open(video_file, "rb") as video:
                bot.send_video(
                    message.chat.id,
                    video,
                    caption="⚡ Yuklab berildi: @tijey_official_\n🚀 Dasturchi: TIJEY Studio"
                )
            bot.delete_message(message.chat.id, status_msg.message_id)
        else:
            bot.edit_message_text("⚠️ Video topilmadi yoki post faqat rasmdan iborat.", chat_id=message.chat.id, message_id=status_msg.message_id)

    except Exception as e:
        logger.error(f"Error downloading {shortcode}: {e}")
        try:
            bot.edit_message_text(
                "❌ Videoni yuklashda xatolik yuz berdi. Post yopiq (private) profil bo'lishi mumkin.",
                chat_id=message.chat.id,
                message_id=status_msg.message_id
            )
        except Exception:
            pass
    finally:
        # Clean up temporary download folder
        if os.path.exists(shortcode):
            shutil.rmtree(shortcode, ignore_errors=True)

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("[FATAL] BOT_TOKEN yo'q, bot ishga tusha olmaydi.")
    else:
        logger.info("Bot muvaffaqiyatli ishga tushdi...")
        bot.infinity_polling()
