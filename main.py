from telegram.ext import ConversationHandler, Filters, MessageHandler, Updater, CommandHandler
from config import TOKEN
from commands.start import start
from message.message import get_phone, cancel
from state import ASK_PHONE
from state import ASK_PHONE


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
            ASK_PHONE: [
                MessageHandler(Filters.contact, get_phone)
            ],
        },

        fallbacks=[CommandHandler("cancel", cancel)],
    )

    dispatcher.add_handler(conv_handler)



    updater.start_polling()
    print("Bot is running...")
    updater.idle()


if __name__ == "__main__":
    main()
