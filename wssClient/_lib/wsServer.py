class wssServer:
	cacheCon = [
		'0.0.0.0',
		8080
	]
	wsHeaders = {
		'Origin': 'https://xat.com'
	}

	print('[Proxying', cacheCon[0] + ':' + str(cacheCon[1]), str(int(time())) + ']')

	def __init__(self):
		self.sendCache()

	def sendCache(self):
		xSock = socket(AF_INET, SOCK_STREAM)
		xSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
		xSock.bind((self.cacheCon[0], self.cacheCon[1]))
		xSock.listen(0)

		if xSock.accept():
			xatSock, xatAddr = xSock.accept()
			xatRecv = xatSock.recv(4096).decode('utf-8', 'ignore')
			print('Accepted connection from {}:{}'.format(xatAddr[0], xatAddr[1]))

			if 'wss.xatbox.com' in xatRecv:
				'''
					To-do:
						If detected, serve V2 with correct cert.
				'''
				self.startConn()
			else:
				print(xatRecv)
				self.send(xatSock, 'Client is running.', 'text/hhtml')

			server = Thread(target = self.sendCache)
			server.start()

		xatSock.close()

	def startConn(self):
		#print('Websocket Detected\n')
		#asyncio.run(self.wsIO())

		wssHeaders = {
			'Host': 'wss.xatbox.com',
			'Connection': 'Upgrade',
			'Pragma': 'no-cache',
			'Cache-Control': 'no-cache',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
			'Upgrade': 'websocket',
			'Origin': 'https://xat.com'
		}

	def send(self, usock, text, mime):
		usock.send((self.sendHeaders.format(mime) + text + "\n").encode('utf-8'))
		usock.close()

wssServer()