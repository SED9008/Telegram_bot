import telegram
import urllib.request
from tinydb import TinyDB, Query, where

class BotHelper:
	def __init__(self, bot):
		self.db 	= TinyDB('db.json')
		self.bot 	= bot

	def executeAssignment(self, chat_id, assignment):
		if assignment['command'] == 'add':
			entries = Query()
			if self.db.search(entries.trigger == assignment['trigger']):
				self.bot.sendMessage(chat_id=chat_id, text='No duplicates allowed for now')
				return False
			else:
				if assignment['response_type'] == 'image' or assignment['response_type'] == 'gif':
					filename 	= assignment['response'].split('/')[-1]
					extention 	= filename.split('.')[-1]
					urllib.request.urlretrieve(assignment['response'], 'media/images/' + assignment['trigger'] + '.' + extention)
					assignment['response'] = 'media/images/' + assignment['trigger'] + '.' + extention

				self.db.insert({
								'trigger':		assignment['trigger'],
								'response_type':assignment['response_type'],
								'response':		assignment['response'],
								})
		if assignment['command'] == 'del':
			self.db.remove(where('trigger') == assignment['trigger'])
		if assignment['command'] == 'list':
			entries = self.db.all()
			for entry in entries:
				self.bot.sendMessage(chat_id=chat_id, text=entry)

	def executeTrigger(self, chat_id, message):
		words 	= message.split(' ') 
		entries = Query()
		for word in words:
			entry = self.db.search(entries.trigger == word)
			if entry:
				if entry[0]['response_type'] == 'text':
					self.bot.sendMessage(chat_id=chat_id, text=entry[0]['response'])
				if entry[0]['response_type'] == 'image':
					img = open(entry[0]['response'], 'rb')
					self.bot.sendPhoto(chat_id=chat_id, photo=img)
				if entry[0]['response_type'] == 'gif':
					img = open(entry[0]['response'], 'rb')
					self.bot.sendDocument(chat_id=chat_id, document=img)