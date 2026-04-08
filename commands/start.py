from telegram import Update
from telegram.ext import CallbackContext
from state import ASK_PHONE

def start(update: Update, context: CallbackContext):
    button = [[{"text": "Raqamni yuborish", "request_contact": True}]]
    text = f"Assalomu alaykum, {update.effective_user.first_name}! Botga xush kelibsiz. "
    update.message.reply_text(text)
    update.message.reply_text("Iltimos, raqamingizni yuboring:", reply_markup={"keyboard": button, "one_time_keyboard": True, "resize_keyboard": True})

    return ASK_PHONE
