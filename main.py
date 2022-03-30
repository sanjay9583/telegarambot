from telegram.ext import *
import Constants as keys
import Responses as R

print("[+] Starting bot...")

def start(update, context):
    update.message.reply_text("Welcome to the world with magical things and I am here to guide you through the world of magic.")
    
def echo(update, context):
    update.message.reply_text(R.sample_response(update.message.text))
    
def handle_message(update, context):
    print("[+] Message received: " + update.message.text)
    update.message.reply_text(R.sample_response(update.message.text)) 
    
def error(update, context):
    """Log Errors caused by Updates."""
    print('Update "%s" caused error "%s"', update, context.error)            

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
main()
        