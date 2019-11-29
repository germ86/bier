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

def
	try:
		search_results_bier = twitter.search(q="#BierbotHelp OR #BierforceHelp", result_type='recent', lang='de',count=20)
		for tweet in search_results_bier['statuses']:
			uid = tweet['id']
			
			username = tweet['user']['screen_name'].encode('utf-8')
			print username
			statushead = "@"+username+" "
			if uid == 
				text = "Hallo Welt! Ich bin ein kleiner Bot!"
				twitter.update_status(status=statushead+text,in_reply_to_status_id=uid)
			else
				text = "Error: 401 Not Authorized"
				twitter.update_status(status=statushead+text,in_reply_to_status_id=uid)
			
	except TwythonError as e:
		print e
