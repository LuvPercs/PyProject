from requests import *
from json import dumps

class test:
	def __init__(self):
		url = 'https://xat.com/web_gear/chat/ip3.php'
		connect = 'https://xat.com/web_gear/chat/ip3.php'

		if url[:7] == '/proxy/':
			self.do_proxy(url, prot)
			return

		if '://' in connect:
			connect = connect[connect.find('://') + 3:]

		if '/' in connect:
			connect = connect.split('/', 1)

			if connect[1][14:16] == 'ip':
				recv = get('https://xat.com/' + connect[1])

				print(self.updateIP3())

	def updateIP3(self):
		source = get('https://xat.com/web_gear/chat/ip3.php')
		replace = source.json()
		replace['E0'] = [1, ['127.0.0.1:' + str('8080') + ':1']]
		replace['E1'] = [1, ['127.0.0.1:' + str('8080') + ':1']]
		return dumps(replace)

test()