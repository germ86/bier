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

from retweet import *
from bothelp import *

#timeline = twitter.getUserTimeline()
#lastEntry = timeline[0]
#sid = str(lastEntry['id'])
#search = twitter.searchTwitter(q="#Bierforce", since_id=sid, rpp="10")


  
  
while True:
	bothelp()
	#reply_to_tweets()
	#rt_user()
	#reply_to_bierforce()
	#retweet_globukalypse()
	#retweet_twankenhaus()
	time.sleep(30)
	
  
