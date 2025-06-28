from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Конфигурация
SOURCE_CHAT_ID = -1002825347288  # Группа-источник
SOURCE_THREAD_ID = 289            # Тема-источник
TARGET_CHAT_ID = -1002278292180   # Группа-получатель
BOT_TOKEN = "7804555297:AAH7YFsNeJeSo5-fyVWybbAjut6VSnF96Sw"      # Замените на свой токен

# Обработчик новых сообщений
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (
        update.effective_chat.id == SOURCE_CHAT_ID
        and update.message.message_thread_id == SOURCE_THREAD_ID
    ):
        await context.bot.send_message(
            chat_id=TARGET_CHAT_ID,
            text=f"📩 Новое сообщение:\n\n{update.message.text}",
        )

# Запуск бота
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    app.run_polling()

if __name__ == "__main__":
    main()
