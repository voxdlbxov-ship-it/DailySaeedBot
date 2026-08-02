import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8950654944:AAEiHQidHlJ0BSp8gcjrHu-CFMd8dmHXVC4"

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
async def months(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["فروردین", "اردیبهشت", "خرداد"],
        ["تیر", "مرداد", "شهریور"],
        ["مهر", "آبان", "آذر"],
        ["دی", "بهمن", "اسفند"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "ماه مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup
    )
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Regex("📅 انتخاب ماه"), months))
app.run_polling()
