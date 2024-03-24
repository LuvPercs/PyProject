from socks import socksocket, setdefaultproxy, PROXY_TYPE_HTTP, PROXY_TYPE_SOCKS5
from socket import socket, AF_INET, SOCK_STREAM, SOL_TCP
from xml.etree.ElementTree import fromstring as xParse
from random import random, randint as rand, choice
from threading import Thread, active_count
from select import select
from requests import get
from json import dumps
from time import sleep
from os import system
from sys import argv
import ntpath
import sys
import math
import os

sys.stderr = ''
system('title Multi-Threaded Xat Raid')
print('/* Written by LuvPercs @github/LuvPercs */\n')

reqData = [
	'_lib/raidLib.py',
	'_lib/_inc/Proxies.txt',
	'_lib/_inc/IDs.txt',
	'_lib/_inc/Insults.txt'
]

exec(open(reqData[0]).read())
P, I = open(reqData[1], 'r').read().split('\n'), open(reqData[2], 'r').read().split('\n')

ActiveThreads = []
[ActiveThreads.append(Thread(target = raidLib, args = [Proxy, ID])) for Proxy, ID in zip(P, I)]

for tH in ActiveThreads: tH.start()

raidLib = raidLib()
raidLib.init()