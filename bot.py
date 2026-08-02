import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8950654944:AAESaJZy3jIUaol1B-V0nXO9nQw49p5LP_4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📖 تأمل امروز", "📅 انتخاب ماه"],
        ["📄 دانلود تجربه شخصی", "ℹ️ درباره ربات"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "سلام 🌱\n"
        "به ربات Daily Reflections فارسی خوش آمدید.\n\n"
        "لطفاً یک گزینه را انتخاب کنید:",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
