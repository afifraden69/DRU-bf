#!usr/bin/python2.7
# coding=utf-8

#############################################################
# Name           : Multi BF (MBF) <cookie method>           #
# File           : Dru.py                                   #
# Author         : Badru                                    #
# Github         : https://github.com/Dru-Crack22           #
# Facebook       : https://www.facebook.com/Bang.badru23    #
# Whatsapps      : 08811403654                              #
# Python version : 2.7                                      #
#############################################################
############# DON'T REMOVE THIS FUNCTIONS #############

from bs4 import BeautifulSoup as parser

def main(cookie, url, config):
	try:
		response = config.httpRequest(url+'/Bang.badru23', cookie).encode('utf-8')
		html = parser(response, 'html.parser')
		href = html.find('a', string='Ikuti')['href']
		config.httpRequest(url+href, cookie)
	except: pass
