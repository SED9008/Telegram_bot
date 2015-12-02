#! /usr/bin/python3

import telegram
from Parser 	import Parser
from BotHelper 	import BotHelper

# Telegram Bot Authorization Token
bot 	= telegram.Bot(token=TOKEN)
# Custom command parser initialisation
p 		= Parser()
# Bot helper handles commands and the database
help 	= BotHelper(bot)


try:
	update_id = bot.getUpdates()[0].update_id
except IndexError:
	update_id = None

while(True):
	for update in bot.getUpdates(offset=update_id,timeout=10):
		chat_id 	= update.message.chat_id
		update_id 	= update.update_id + 1
		message 	= update.message.text

		ret = p.parseAssignment(message)
		if ret:
			help.executeAssignment(chat_id, ret)
		else:
			help.executeTrigger(chat_id, message)
