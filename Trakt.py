import urllib2
import re
import sys
import simplejson
import sys
import os

#---[ Config ]---#

apikey = "ADD API KEY HERE"

#---[ Code ]-----#

def gerarLista(url):
	json = urllib2.urlopen(url).read()
	(true,false,null) = (True,False,None)
	return eval(json)

def perguntar():
	os.system('clear')
	print " ----------------------------------------------------------------------"
	print "|  Chose a option:                                                     |"
	print "|  [1] List your watchlist                                             |"
	print "|  [2] List watched movies                                             |"
	print "|  [3] Compare watchlist between two users                             |"
	print " ---------------------------------------------------------------------#"
	option =  int(raw_input("| Your option: "))

	if option == 1:
		print " ---------------------------------------------------------------------#"
		username =  raw_input("| Your username: ")
		print " ---------------------------------------------------------------------#"
		lista = gerarLista("http://api.trakt.tv/user/watchlist/movies.json/" + apikey  + "/" + username)

		i = 1
		for x in lista:
			print "| " + str(i) + " - ("+ str(x['year']) + ")" +  " - " + x['title'] 
			i=i+1

		raw_input("| Press enter to return ##############################################")
		perguntar()

	elif option == 2:
		print " ---------------------------------------------------------------------#"
		username =  raw_input("| Your username: ")
		print " ---------------------------------------------------------------------#"
		lista = gerarLista("http://api.trakt.tv/user/library/movies/watched.json/" + apikey  + "/" + username)

		i = 1
		for x in lista:
			print "| " + str(i) + " - ("+ str(x['year']) + ")" +  " - " + x['title'] 
			i=i+1

		raw_input("| Press enter to return ##############################################")
		perguntar()

	elif option ==3:
		print " ---------------------------------------------------------------------#"
		usr1 = raw_input("| First user: ")
		usr2 = raw_input("| Second user: ")

		print " ---------------------------------------------------------------------#"
		print '| Searching: ' + usr1.upper() + ' / ' + usr2.upper()

		listaUSR1 = gerarLista("http://api.trakt.tv/user/watchlist/movies.json/" + apikey  + "/" + usr1)
		listaUSR2 = gerarLista("http://api.trakt.tv/user/watchlist/movies.json/" + apikey  + "/" + usr2)

		print " ---------------------------------------------------------------------#"

		i = 1
		for x in listaUSR1:
			for k in listaUSR2:
				if x['title'] == k['title']:
					print "| " + str(i) + " - ("+ str(x['year']) + ")" +  " - " + x['title']
					i = i+1

		print " ---------------------------------------------------------------------#"

		raw_input("| Press enter to return ##############################################")
		perguntar()
	else:
		perguntar()

perguntar()
