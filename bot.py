import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

MONTH_DAYS = {
    "فروردین": 31,
    "اردیبهشت": 31,
    "خرداد": 31,
    "تیر": 31,
    "مرداد": 31,
    "شهریور": 31,
    "مهر": 30,
    "آبان": 30,
    "آذر": 30,
    "دی": 30,
    "بهمن": 30,
    "اسفند": 29,
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📖 تأمل امروز", "📅 انتخاب ماه"],
        ["📄 دانلود تجربه شخصی", "ℹ️ درباره ربات"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )

    await update.message.reply_text(
        "سلام 🌱\n"
        "به ربات Daily Reflections فارسی خوش آمدید.\n\n"
        "لطفاً یک گزینه را انتخاب کنید:",
        reply_markup=reply_markup,
    )


async def months(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["فروردین", "اردیبهشت", "خرداد"],
        ["تیر", "مرداد", "شهریور"],
        ["مهر", "آبان", "آذر"],
        ["دی", "بهمن", "اسفند"],
        ["🔙 بازگشت"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )

    await update.message.reply_text(
        "ماه مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup,
    )


async def show_days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    month = update.message.text

    if month not in MONTH_DAYS:
        return

    days = MONTH_DAYS[month]

    keyboard = []
    row = []

    for day in range(1, days + 1):
        row.append(str(day))

        if len(row) == 7:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append(["🔙 انتخاب ماه"])

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
    )

    context.user_data["selected_month"] = month

    await update.message.reply_text(
        f"📅 {month}\n\n"
        "روز مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup,
    )


async def show_reflection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text.isdigit():
        return

    month = context.user_data.get("selected_month")

    if not month:
        return

    day = int(text)

    await update.message.reply_text(
        f"📖 تأمل روز {day} {month}\n\n"
        "متن تأمل این روز هنوز به ربات اضافه نشده است.\n\n"
        "در مرحله بعد، متن تأمل‌های روزانه را وارد می‌کنیم. 🌱"
    )


async def back_to_months(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await months(update, context)


async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


app = Application.builder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    MessageHandler(
        filters.Regex("^📅 انتخاب ماه$"),
        months,
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex(
            "^(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|"
            "مهر|آبان|آذر|دی|بهمن|اسفند)$"
        ),
        show_days,
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex(r"^\d+$"),
        show_reflection,
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex("^🔙 انتخاب ماه$"),
        back_to_months,
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex("^🔙 بازگشت$"),
        back_to_start,
    )
)

app.run_polling()
