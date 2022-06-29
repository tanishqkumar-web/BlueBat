from telegram.ext import *
import SecretKey as key
import Responses as R
import sys
import subprocess 



print("~~~Bot Starting~~~")

def start_command(update, context):#/start
    update.message.reply_text('Hi!\nhi👋\n~I am a Blue Bat that does bat stuff')

def help_command(update, context): #/help
    update.message.reply_text('I am a growing bat\nfor now to require assistance, \nplease contact my caretakers via: helpers_out_of_the_blue@protonmail.com')

def python_output(message):
    try:
        print("It entered this stage")

        f= open("program.py", "a")
        f.truncate(0)
        f.write(message+"\n")
        f.close()

        output = subprocess.check_output([sys.executable, './program.py'])
        tp = open('outfile.txt', 'wb')
        with tp as outfile:
            outfile.write(output)
        tp.close()
            

    except:
        sorry= "There was an error\nSorry--Sorry\ni tried my best🙁"
        update.message.reply_text(sorry)

        print(sorry)
        print(f"Update {update} caused error {context.error}")

def handle_message(update, context):
    chat_text = str(update.message.text).lower()
    response = R.sample_responses(chat_text)
#Python Output
    if chat_text[:3] == "#py":

        python_output(update.message.text) 

        rd = open('outfile.txt','r')
        out = rd.readlines()
        for line in out:
            update.message.reply_text(line)
        rd.close()


#Echo
    if chat_text[:3] != "#py" and response == False:
        update.message.reply_text(update.message.text)
        
#Response
    elif chat_text[:3] != "#py" and response!= False:
            update.message.reply_text(response)
        


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(key.API_KEY, use_context= True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
main()