from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import ConversationHandler

GENDER, AGE, BIO = range(3)

def start_registration(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Чтобы зарегистрироваться, напишите свой пол. Например, "Мужчина", "Женщина" или "Другой".'
    )
    return GENDER

def receive_gender(update: Update, context: CallbackContext) -> int:
    context.user_data['gender'] = update.message.text
    update.message.reply_text('Теперь укажите свой возраст.')
    return AGE

def receive_age(update: Update, context: CallbackContext) -> int:
    context.user_data['age'] = update.message.text
    update.message.reply_text('Напишите немного о себе.')
    return BIO

def receive_bio(update: Update, context: CallbackContext) -> int:
    context.user_data['bio'] = update.message.text
    update.message.reply_text('Спасибо! Регистрация завершена.')
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Регистрация отменена.')
    return ConversationHandler.END
