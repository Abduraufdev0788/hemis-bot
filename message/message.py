from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from state import ASK_PHONE
from config import BASE_URL
import requests

def get_phone(update: Update, context: CallbackContext):
    contact = update.message.contact

    phone = contact.phone_number
    user_id = contact.user_id

    update.message.reply_text(f"Raqam olindi: {phone}")
    data = {
        "telegram_id": user_id,
        "phone_number": phone,
        "name": update.effective_user.first_name
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        update.message.reply_text("Raqamingiz muvaffaqiyatli saqlandi!")
    else:
        update.message.reply_text("Raqamingiz saqlanishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")


    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Bekor qilindi.")
    return ConversationHandler.END