class wsBot(Thread):
	global getBetween

	def __init__(self, socket, port):
		Thread.__init__(self)
		self.daemon = True

		self.sockets = [socket[0]]
		self.port = int(port)

		self.users = {}
		self.packetDump = {
			'log_client': False,
			'log_server': False
		}

	def run(self):
		try:
			global xatlib