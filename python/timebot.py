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

def uhrzeit():
	try:
		#seconds = time.time()
		#print ("Sekunden vergangen seit: ", seconds)
		named_tuple = time.localtime()		
		time_string = time.strftime("%H:%M:%S -- %H.%m.%Y", named_tuple)
		print time_string
	except TwythonError as e:
		print e

def timebot():
	try:
		
		print "BierbotTime Start"
		named_tuple = time.localtime()		
		#time_string = time.strftime("%H:%M:%S -- %H.%m.%Y", named_tuple)
		time_string = time.strftime("%H:%M:%S", named_tuple)	
		search_results_bier = twitter.search(q="#BierbotTime")
		for tweet in search_results_bier['statuses']:			
			tweetId = data["target_object"]["id_str"]
			print tweetID
			uid = tweet['id']
			text = "Es ist jetzt: "
			username = tweet['user']['screen_name'].encode('utf-8')
			print username
			statushead = "@"+username+" "
			twitter.update_status(status=statushead+text+time_string,in_reply_to_status_id=uid)
			if(time_string == "05:52:00"):
				twitter.update_status(status="Es ist jetzt: " + time_string + " Uhr")
			else:
				print "Zeit Fehler"
	except TwythonError as e:
		print e

while True:
	uhrzeit()
	timebot()
	time.sleep(1)
