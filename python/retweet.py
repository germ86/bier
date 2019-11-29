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

def retweet_globukalypse():
	try:
		search_results_globukalypse = twitter.search(q="#Globukalypse OR #Twankenhaus OR #Twankenhaus4change OR #NehmtEureTabletten -filter:retweets AND -filter:replies -filter:RT", result_type='mixed', lang='de',count=20)
		for tweet in search_results_globukalypse['statuses']:
			
			try:
				if tweet['retweeted'] == 'true':
					print (tweet['retweeted'] == 'true')
					twitter.retweet(id = tweet["id_str"])
					print('Wurde ' +  tweet["id_str"] + ' RT')
					print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
					print tweet['text'].encode('utf-8'),'\n'
				else: 
					print('Tweet ' + tweet["id_str"] + ' wurde retweeted')
					#twitter.retweet(id = tweet["id_str"])
					print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
					print tweet['text'].encode('utf-8'),'\n'
			except TwythonError as e:
				print e
	except TwythonError as e:
		print e   



def rt_user():
	try:
		search_result_user = twitter.search(q="@NatalieGrams OR @drluebbers OR @ApothekerDer OR @twankenhaus OR @EdzardErnst OR @skt_johann OR @AnthroBlogger OR @OnkelBlogs OR @globuleaks OR @pharmamafia OR @rki_de OR @DToxikologe OR @globukalypse -filter:replies -filter:RT since:2019-11-19", result_type='mixed', lang='de',count=100)
		for tweet in search_result_user['statuses']:
			try:
				if tweet['retweeted'] == 'true':
					print('Tweet wird retweeted: User: ' + tweet['user']['screen_name'] )
					twitter.retweet(id = tweet["id_str"])					
				else: 
					#print('Wurde RT: ' + tweet['user']['screen_name'].encode(utf-8), tweet['created_at'] )
					print('Retweetet: ')
					print tweet['text'].encode('utf-8'),'\n'
	
			except TwythonError as e:
				print e
	except TwythonError as e:
		print e
  
