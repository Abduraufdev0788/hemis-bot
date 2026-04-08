from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

def get_phone(update: Update, context: CallbackContext):
    contact = update.message.contact

    phone = contact.phone_number
    user_id = contact.user_id

    update.message.reply_text(f"Raqam olindi: {phone}")


    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Bekor qilindi.")
    return ConversationHandler.END