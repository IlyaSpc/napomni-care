from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🛡️ Вставь сюда свой токен от @BotFather:
BOT_TOKEN = "7956554161:AAFhy7lY7sXbm863aizX-oVo0ucQ9UoFspM"

# 🔗 URL твоего мини-приложения
WEBAPP_URL = "https://napomni-care-qraoxpncv-ilyaspcs-projects.vercel.app"

# 🔁 Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🗓️ Открыть приложение", web_app={"url": WEBAPP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Нажми на кнопку ниже, чтобы открыть приложение:",
        reply_markup=reply_markup
    )

# 🚀 Запуск бота
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
