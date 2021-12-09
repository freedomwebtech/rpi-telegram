
import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
from time import sleep 
GPIO.setwarnings(False)
led_pin = 23

GPIO.setmode(GPIO.BCM) 
GPIO.setup(led_pin, GPIO.OUT)

now = datetime.datetime.now() # Getting date and time

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Received:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    if command == '/hi':
        bot.sendMessage (chat_id, str("Hello World"))
    elif command == '/time':
        bot.sendMessage(chat_id, str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
    elif command == '/date':
        bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))
    elif command == '/led_1':
        bot.sendMessage(chat_id, str("led is ON"))
        GPIO.output(led_pin, True)
    elif command == '/led_0':
        bot.sendMessage(chat_id, str("led is OFF"))
        GPIO.output(led_pin, False)

# Insert your telegram token below
bot = telepot.Bot('5023406108:AAFuYjCMS1RwHBl1tCEWG4C3VN3oEWq6Hzc')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)
