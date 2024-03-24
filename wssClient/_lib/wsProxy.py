class sslProxy(Thread):

	def __init__(self, socket):
		Thread.__init__(self)
		self.daemon = True
		self.socket = socket[0]
		self.wsaddr = ['wss.xatbox.com']

	def run(self):
		global server

		try:
			recv = self.socket.recv(99999)
			print(recv)

			'''parseRecv = recv.split('\r\n')

			CMD, Host, Proxy, UserAgent = parseRecv[0], parseRecv[1], parseRecv[2], parseRecv[3]

			print(CMD, Host, Proxy)

			CMD = CMD.split(' ')
			CMD = [
				CMD[0], # Connect Type
				CMD[1],	# Host
				CMD[2]	# SSL Type
			]

			self.Headers = {
				'Connection': 'Upgrade',
				'Host': 'wss.xatbox.com',
				'Origin': 'https://xat.com',
				'Upgrade': 'websocket',
				'User-Agent': UserAgent
			}

			#print(dumps(Headers))

			if Host.index(self.wsaddr[0]):
				Host = Host.split(' ')
				#print(CMD[2], Host[1])
				#self.do_proxy()'''

			'''if 'wss.xatbox' in recv:
				self.do_proxy('https://wss.xatbox.com/v2', prot)
				return print('Proxying wss', prot)

			if url[:7] == '/proxy.':
				print(url, prot)
				self.do_proxy(url, prot)
				return

			if '://' in connect:
				connect = connect[connect.find('://') + 3:]

			if '/' in connect:
				connect = connect.split('/', 1)

				if connect[1][14:16] == 'ip':
					recv = get('https://xat.com/' + connect[1]).content

					with open('./_cache/xatIPs.txt', 'w') as lolProxy:
						lolProxy.write(self.updateIP3())
						lolProxy.close()

					self.socket.send(bytes(self.updateIP3(), encoding = 'utf-8'))
					self.socket.close()
					return'''

		except (Exception) as e:
			print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

	def updateIP3(self):
		source = get('https://xat.com/web_gear/chat/ip3.php')
		replace = source.json()
		replace['E0'] = [1, ['127.0.0.1:' + str(server.proxy['pt']) + ':1']]
		replace['E1'] = [1, ['127.0.0.1:' + str(server.proxy['pt']) + ':1']]
		return dumps(replace)

	def do_proxy(self):
		self.socket.send(bytes('GET /v2 HTTP/1.1\r\nHost: wss.xatbox.com\r\n\r\n', encoding = 'utf-8'))
		self.socket.close()
		return print('Proxied')