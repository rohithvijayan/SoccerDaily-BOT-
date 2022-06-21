import requests
import newsapi
from telebot import TeleBot

bot=TeleBot("5564377267:AAEUWTaHteOE6-zhIvBA2w6yYfe5iDrgi-g")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Heyy SoccerDaily here!\nGet latest updates from major leagues and tournaments,\nTransfer Updates and Rumours an more:)')
    bot.send_animation(message.chat.id,animation="https://tenor.com/bFRzH.gif")
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Sorry with the issue,will try to resolve soon!')
    bot.send_animation(message.chat.id,animation="https://tenor.com/bCB80.gif")
client=newsapi.NewsApiClient("6e7e06236b6f422ebb6a0fa21532e4c5")
topnews=client.get_top_headlines(sources='four-four-two',language='en',page_size=5,page=1)
articles=topnews['articles']
@bot.message_handler(commands=['news'])
def news(message):
    for dic in articles:
        titles = dic['title']
        urls = dic['url']
        data = titles + ':' + urls
        bot.send_message(message.chat.id,data)
bot.polling()
