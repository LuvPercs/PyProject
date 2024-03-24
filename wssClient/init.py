from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SO_RCVTIMEO, SO_SNDTIMEO
from threading import Thread, activeCount, enumerate as threads
from re import findall as re_findall, sub as re_sub
from xml.etree.ElementTree import fromstring
from websocket import create_connection
from base64 import b64encode, b64decode
from os.path import basename, realpath
from os.path import isfile, getmtime
from traceback import print_exc
from websockets import connect
from time import time, sleep
from random import randint
from requests import *
from math import floor
from json import loads, dumps
from select import select
from gc import collect
from os import system
from glob import glob
import asyncio
import sys

#exec(open("_lib/wsServer.py").read())
exec(open("_lib/wsEnvironment.py").read())
exec(open("_lib/wsProxy.py").read())

server = wssEnvironment()
server.init()