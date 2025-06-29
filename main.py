from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

SOURCE_CHAT_ID = -1002825347288  # Группа-источник
SOURCE_THREAD_ID = 289           # ID темы
TARGET_CHAT_ID = -1002409306862  # Группа-получатель
BOT_TOKEN = "7804555297:AAH7YFsNeJeSo5-fyVWybbAjut6VSnF96Sw"

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (
        update.effective_chat.id == SOURCE_CHAT_ID
        and update.message.message_thread_id == SOURCE_THREAD_ID
    ):
        # Пересылка фото
        if update.message.photo:
            photo = update.message.photo[-1]  # Берем самое высокое качество
            await context.bot.send_photo(
                chat_id=TARGET_CHAT_ID,
                photo=photo.file_id,
                caption=update.message.caption  # Подпись к фото (если есть)
            )
        # Пересылка документов (файлов)
        elif update.message.document:
            await context.bot.send_document(
                chat_id=TARGET_CHAT_ID,
                document=update.message.document.file_id,
                caption=update.message.caption
            )
        # Пересылка текста
        elif update.message.text:
            await context.bot.send_message(
                chat_id=TARGET_CHAT_ID,
                text=f"📩 Сообщение:\n\n{update.message.text}"
            )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    # Фильтр для ВСЕХ сообщений (включая медиа)
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_message))
    app.run_polling()

if __name__ == "__main__":
    main()
