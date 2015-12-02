class Parser:
	def __init__(self):
		self.commands = {
						'add':{
								'args':5,
								},
						'del':{
								'args':3,
								},
						'list':{
								'args':2,
								},
						}

	def parseAssignment(self, message):
		words = message.split(' ')
		if words[0] == '/bot':
			if len(words)> 1:
				for command in self.commands:
					if words[1] == command:
						if words[1] == 'add':
							if len(words) > 4:
								response = words[4]
								for h in range(5, len(words)):
									response = response + ' ' + words[h]
								assignment = {	
												'command':			words[1],
												'trigger':			words[2],
												'response_type': 	words[3],
												'response': 		words[4],
												}
								return assignment
							else:
								print('Not enough args')
								return False
						elif len(words) == self.commands[command]['args']:
							for h in range(0,len(words)):
								if words[h] == '':
									print('Spaces detected:')
									return False
							assignment = {'command':words[1]}
							if command == 'del':
								assignment['trigger'] = words[2]
							return assignment
						else:
							print('Too much or few arguments')
							return False
					# else:
				print('Bad command: ' + words[1])
				return False
			else:
				print('No assignment')
				return False
		else:
			print('No command')
			return False