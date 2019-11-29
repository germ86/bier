from twython import Twython, TwythonError
import time
import logging
logging.debug('Debugging Information')
logging.info('Information')
logging.warning('Warnung:Datei %s nicht gefunden', ' server.conf')
logging.error('Fehler')
logging.critical('Kritischer Fehler!')

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def bothelp():
	try:
		search_results_bier = twitter.search(q="#BierbotHelp OR #BierforceHelp from:@bierbot1", result_type='recent', lang='de',count=20)
		for tweet in search_results_bier['statuses']:
			uid = tweet['id']
			username = tweet['user']['screen_name'].encode('utf-8')
			statushead = "@"+username+" "
			user = bierbot1
			
			if(username == 'user'):
				print username
				print uid
				
				text = "Hallo " + username + " Ich bin ein kleiner Bot! " 
				#text2 = "Hallo " + username + " Ich bin Tweet2!"
				#text3 = "Hallo " + username + " Ich bin Tweet3 !"
				
				twitter.update_status(status=statushead+text,in_reply_to_status_id=uid,)

			else:
				print username
				print uid
				#print ("Userid: "+ uid + "Username: " + username)
				text = "Error: 401 Not Authorized"
				twitter.update_status(status=statushead+text,in_reply_to_status_id=uid)
			  
	except TwythonError as e:
		print e
