from random import randint as rand
from urllib import parse
from hashlib import md5
import requests

class Speedy:
	sendData = {
		0: str(rand(3000, 3999)) + str(rand(100, 200)), # Upload
		1: str(rand(4000, 4999)) + str(rand(100, 200)),	# Download
		2: str(rand(1, 5)),				# Ping
		3: 43932,					# Server
		4: 8, 						# Accuracy
		5: {
			'Host': 		'www.speedtest.net',
			'User-Agent': 		'Speedtest',
			'Content-Type': 	'application/x-www-form-urlencoded',
			'Origin': 		'http://c.speedtest.net',
			'Referer': 		'http://c.speedtest.net/flash/speedtest.swf',
			'Cookie': 		'',
			'Connection': 		'Close'
		},
		6: ['http://www.speedtest.net/api/api.php']
	}

	def __init__(self):
		print('[Data]', 'Up: {}, Dl: {}, Ping: {} ms'.format(self.sendData[0], self.sendData[1], self.sendData[2]))

		buildStr = '{}-{}-{}-297aae72'.format(self.sendData[2], self.sendData[0], self.sendData[1])

		hash = md5()
		hash.update(bytes(buildStr, 'utf-8'))
		hash = hash.hexdigest()

		dataStr = 'startmode=recommendedselect&promo=&upload={}&accuracy={}&recommendedserverid={}&serverid={}&ping={}&hash={}&download={}'.format(self.sendData[0], self.sendData[4], self.sendData[3], self.sendData[3], self.sendData[2], hash, self.sendData[1])

		post = requests.post(self.sendData[6][0], headers = self.sendData[5], data = dataStr)
		post = str(post.content)

		for chunk in post.split('&'):
			param = chunk.split('=')

			if parse.unquote(param[0]) == 'resultid':
				print('[Link]', 'http:/www.speedtest.net/my-result/{}.png'.format(parse.unquote(param[1])))

Speedy()
