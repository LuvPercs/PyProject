class wssEnvironment:
	sockets = {}
	proxy = {
		'ip': '127.0.0.1', 'pt': 8081, '_pt': 80
	}

	def __init__(self):
		thread = Thread(target = self.clear)
		thread.daemon = True
		thread.start()

		#for port in range(8080, 8081):
		print('[Bind]', str(self.proxy['ip']) + ':' + str(self.proxy['pt']), str(self.proxy['_pt']))
		_socket = socket(AF_INET, SOCK_STREAM)
		_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
		_socket.bind((str(self.proxy['ip']), self.proxy['pt']))
		_socket.listen(1000)
		self.sockets[_socket] = self.proxy['pt']
		
		'''_socket = socket(AF_INET, SOCK_STREAM)
		_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
		_socket.bind((str(self.proxy['ip']), self.proxy['_pt']))
		_socket.listen(25)
		self.sockets[_socket] = self.proxy['_pt']'''

		while True:
			try:
				waiting = select(self.sockets, [], [], None)

				for _socket in waiting[0]:
					try:
						if self.sockets[_socket] == 8081:
							print('[WS][Loaded] -> wsProxy')
							sslProxy(_socket.accept()).start()
					except (Exception) as e:
						print(e)
					#else:
						#pass
						#wsBot(_socket.accept(), self.sockets[_socket]).start()
			except (Exception) as e:
				print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

	def clear(self):
		while True:
			collect()
			sleep(10)