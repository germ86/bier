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



get_list = twitter.get_direct_messages()
#Returns All Twitter DM information which is a lot in a list format

dm_dict = get_list[0]
#Sets get_list to a dictionary, the number in the list is the direct message retrieved
#That means that 0 is the most recent and n-1 is the last DM revieved.
#You can cycle through all the numbers and it will return the text and the sender id of each

print (dm_dict['text'])
#Gets the text from the dictionary

print (dm_dict['sender']['id'])
#Gets the ID of the sender


#text = "Ich bin eine Bot DM"
#uid = message_create.target.recipient_id = '809806959796948992'
#message_create.message_data = text

#twitter.send_direct_messages(uid, message_create.message_data = 'text')
