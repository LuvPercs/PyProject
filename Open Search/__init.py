from collections import OrderedDict
from os import system
import socket as sock
import configparser
import requests
import ntpath
import time
import json
import os

system('title a0_0x4374 f8o5WQLoW6/cLCopW7xcI0m')

class loadAPI:
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__)) + '/_inc/mainconf.ini')

    globalRoot = '[' + config['LOGIN']['Usr'] + '@' + os.getlogin() + '\\' + ntpath.basename(os.path.dirname(os.path.abspath(__file__))) + '] ~ '
    globalLoc = os.path.dirname(os.path.abspath(__file__)) + '/_inc'

    logToken = ''

    def __init__(self):
        print(self.globalRoot)

        self.buildAuthenticationToken()
        self.logToken = self.buildAuthenticationToken()
  
        while True:
            print(self.globalRoot)

            addressInfo = {
                'address': input('\tAddress -> '),
                'city': input('\tCity -> '),
                'state': 'MI'
            }

            self.returnInfoValues(addressInfo['address'], addressInfo['city'], addressInfo['state'])

    def buildAuthenticationToken(self):
        authHeader = {
            'Accept': '*/*',
            'Authorization': 'Bearer ' + self.config['BEARER']['Token'],
            'Content-Type': 'application/json'
        }

        authData = '{"username":"' + self.config['LOGIN']['User'] + '","password":"' + self.config['LOGIN']['Pass'] + '"}'

        sendLogin = requests.post(self.config['API']['apiAuth'], headers = authHeader, data = authData)
        loginResponse = sendLogin.json()
        self.responseTime = sendLogin.status_code

        return loginResponse['token'];

    def returnInfoValues(self, address, city, state):
        print('\n')
        logData = open(self.globalLoc + '/LOGS.txt', 'a')

        headersAPI = {
            'Accept': 'text/plain',
            'Authorization': 'Bearer ' + self.buildAuthenticationToken(),
            'Content-Type': 'application/json'
        }

        dataAPI = '{"address":"' + address + '","unit":"","city":"' + city + '","state":"' + state + '"}'

        getInformation = requests.post(self.config['API']['apiPSR'], headers = headersAPI, data = dataAPI)
        serverResponse = getInformation.json()
        seen = OrderedDict()
        numData = 0

        for data in serverResponse['results']:
            pName = data['firstName']
            numData = numData + 1

            if pName not in seen:
                logData = open(self.globalLoc + '/LOGS.txt', 'a')

                seen[pName] = data
                print('\t' + str(numData) + ' -> ' + data['firstName'] + ' ' + data['lastName'] + '\n\t\tDOB: ' + data['dob'] + '\n\t\tAgency: ' + data['agencyName'] + ' - ' + str(data['recordId']))

        logData.write(f"{self.globalRoot}\nLogin Token: {self.logToken}\n{serverResponse}\n\n")
        logData.close()

        print('\n\n')

loadAPI()