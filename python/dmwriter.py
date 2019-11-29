from twython import Twython, TwythonError
import time
import os, sys, re
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

text = ("Der B.I.E.R Bot soll als Übungsprojekt dienen. Jeder darf sich beteiligen. Sei es #development (#APIs, #App, #Frontend \/#Backend ), Auswertung und #Statistik, #design, #Dokumentation oder auch andere Dinge. Es soll #opensource \/ #openscience sein.

#followerpower #plRt")

twitter.update_status(status=text)

#direct_message = api.send_direct_message(user=username, text=message_text)
