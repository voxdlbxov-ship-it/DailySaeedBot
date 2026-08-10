import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "8950654944:AAEiHQidHlJ0BSp8gcjrHu-CFMd8dmHXVC4"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📖 تأمل امروز", "📅 انتخاب ماه"],
        ["📄 دانلود تجربه شخصی", "ℹ️ درباره ربات"],
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
        ["دی", "بهمن", "اسفند"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "ماه مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup
    )


async def select_month(update: Update, context: ContextTypes.DEFAULT_TYPE):
    month = update.message.text

    months_list = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]

    if month not in months_list:
        return

    context.user_data["selected_month"] = month

    keyboard = []
    row = []

    for day in range(1, 32):
        row.append(str(day))

        if len(row) == 7:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        f"ماه {month} انتخاب شد.\n\n"
        "روز مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup
    )


async def show_reflection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text.isdigit():
        return

    month = context.user_data.get("selected_month")

    if not month:
        return

    day = int(text)

    if month == "فروردین" and day == 1:
        await update.message.reply_text(
            "📖 خوشبختی مادی و معنوی\n\n"
            "ترس از ناامنی اقتصادی ما را ترک خواهد کرد.\n\n"
            "(الکلی‌های گمنام)\n\n"
            "کم شدن یا از بین رفتن ترس و بهبود وضعیت اقتصادی دو مقوله متفاوت هستند. "
            "وقتی که تازه به انجمن وارد شده بودم، این دو موضوع را با هم قاطی می‌کردم. "
            "فکر می‌کردم ترس تنها زمانی مرا رها خواهد کرد که پول داشته باشم.\n\n"
            "اما یک روز که غرق در مشکلات اقتصادی بودم، جمله دیگری از کتاب جامع بیرون پرید:\n\n"
            "«در نظر ما سعادت مادی همیشه به دنبال رشد معنوی می‌آید، نه پیش از آن.»\n\n"
            "ناگهان فهمیدم که این یک نوع ضمانت است. دیدم که این کتاب اولویت‌ها را "
            "به ترتیب درستی چیده است. دیدم که پیشرفت معنوی آن ترس‌های وحشتناک از "
            "نیازمندی را از بین می‌برد، همان‌طور که بسیاری از ترس‌های دیگر را نابود کرده است.\n\n"
            "حالا سعی می‌کنم از استعدادهایی که خداوند به من عطا کرده به نفع دیگران استفاده کنم. "
            "به این نتیجه رسیده‌ام که این چیزی است که برای دیگران ارزشمند است.\n\n"
            "سعی می‌کنم همیشه به خاطر داشته باشم که من دیگر برای خودم کار نمی‌کنم. "
            "من فقط از نعمت‌هایی که خداوند برایم آفریده استفاده می‌کنم، من هرگز صاحب آنها نیستم.\n\n"
            "وقتی کار می‌کنم تا کمک کنم، نه اینکه صاحب شوم، هدف زندگی‌ام روشن‌تر می‌شود. 🌱"
        )
        return

    if month == "فروردین" and day == 2:
        await update.message.reply_text(
            "📖 درگیری‌ها را کنار گذاشتیم\n\n"
            "و ما درگیری بر سر هر چیز یا با هر کسی را کنار گذاشتیم، حتی بر سر الکل.\n\n"
            "(الکلی‌های گمنام)\n\n"
            "وقتی انجمن مرا یافت، فکر می‌کردم در انجمن هستم تا آماده درگیری شوم و اینکه انجمن می‌خواهد قدرت لازم برای شکست الکل را به من بدهد. "
            "اگر در این نبرد پیروز شوم چه کسی می‌داند در چه نبردهای دیگری هم می‌توانم برنده شوم. "
            "اما باید قوی باشم. تجربیات زندگی این را به من ثابت کرده بود.\n\n"
            "امروز، مجبور نیستم بجنگم یا اراده‌ام را تحمیل کنم. "
            "اگر آن دوازده گام را به کار بندم و بگذارم تا نیروی برترم کارش را انجام دهد، مشکل الکلیسم خود به خود ناپدید می‌شود.\n\n"
            "دیگر مجبور نیستم با مشکلات زندگی‌ام دست و پنجه نرم کنم. "
            "فقط باید بپرسم که آیا پذیرش یا تغییر ضروری است. "
            "این اراده من نیست، بلکه اراده خداوند است که باید کارها را انجام دهد."
        )
        return

async def back_to_months(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await months(update, context)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.Regex("^📅 انتخاب ماه$"),
        months
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex(
            "^(فروردین|اردیبهشت|خرداد|تیر|مرداد|شهریور|مهر|آبان|آذر|دی|بهمن|اسفند)$"
        ),
        select_month
    )
)

app.add_handler(
    MessageHandler(
        filters.Regex(r"^\d+$"),
        show_reflection
    )
)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        pass


def run_health_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


Thread(target=run_health_server, daemon=True).start()

app.run_polling()
