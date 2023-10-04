from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '5992271347:AAH5ocnnXXeFNRM8wF40Ch8zg6Rdk29JM2Y'
BOT_USERNAME: Final = '@p0tabot'
# commands here:
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there. What your potato mind says?')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('How to help?')



async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')



# resposes:
# eikhanei sob add kora jane AI aro onno kisu
def handle_respose(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'hey there'

    if 'how are you' in processed:
        return 'i am fine. what about you?'

    if 'fine' in processed:
        return 'glad to know'

    return 'I do not understand what you worte...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            respose: str = handle_respose(new_text)
        else:
            return
    else:
        resonse: str = handle_respose(text)

    print('Bot:', resonse)
    await update.message.reply_text(respose)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__=='__main__':
    print('staring bot...')
    app= Application.builder().token(TOKEN).build()
    # commands

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # error handler

    app.add_error_handler(error)
    # polling
    print('polling...')
    app.run_polling(poll_interval=5)


