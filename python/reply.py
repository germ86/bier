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

def reply_to_tweets():
	try:
		search_results = twitter.search(q="#Bierforce", count=20)
		
		for tweet in search_results['statuses']:
			
		  print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
		  print tweet['text'].encode('utf-8'), '\n'
		  tweetID = tweet['id']
		  print tweetID
		  
			#text = "@" + tweet['user']['screen_name'] + " " + "Hallo Welt! Ich bin der B.I.E.R Bot!"
		  text = "Hallo Welt! Ich bin der B.I.E.R Bot!"
		 	#statushead = '@'+ tweet['from_user'] + " "
		  twitter.update_status(status=text,in_reply_to_status_id=tweetID)
  
	except TwythonError as e:
		print e
  
  
def reply_to_bierforce():
	try:
		search_results_bier = twitter.search(q="#BierbotHelp OR #Bierforce OR B.I.E.R OR B.I.E.R. -filter:retweets AND -filter:replies -filter:RT", result_type='recent', lang='de',count=20)
		for tweet in search_results_bier['statuses']:
			uid = tweet['id']
			text = "Hallo Welt! Ich bin ein kleiner Bot!"
			username = tweet['user']['screen_name'].encode('utf-8')
			print username
			statushead = "@"+username+" "
			twitter.update_status(status=statushead+text,in_reply_to_status_id=uid)
	except TwythonError as e:
		print e
