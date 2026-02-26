from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

import os
TOKEN = os.environ.get("BOT_TOKEN")

FILES = {
    "1001": "video1.mp4",
    "1002": "story1.jpg"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋\nکد محتوا رو بفرست:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()

    if code in FILES:
        file_path = os.path.join("files", FILES[code])

        if os.path.exists(file_path):
            await update.message.reply_document(document=open(file_path, "rb"))
        else:
            await update.message.reply_text("فایل پیدا نشد ❌")
    else:
        await update.message.reply_text("کد نامعتبره ❌")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("ربات اجرا شد...")
app.run_polling()