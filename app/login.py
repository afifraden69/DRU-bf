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
import os, time
from src import language

def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	print('\n[©] Login Pakai FB cookie Kalian : [©]\n')
	while True:
		cookies = raw_input('Masukan Cookie Facebook Kalian: ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\nTunggu Beberapa Detik...')
			language.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			print('\n\033[0;92mLogin Berhasil✓\033[0m')
			time.sleep(2)
			break
		else:
			print('\n\033[0;91mCookie Salah, Coba Lagi.\n\033[0m')
