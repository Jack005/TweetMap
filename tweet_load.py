#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import codecs
import glob
import json
import re

#Variables that contains the user credentials to access Twitter API
access_token = "*"
access_token_secret = "*"
consumer_key = "*"
consumer_secret = "*"

import boto.cloudsearch2
import json
from boto.cloudsearch2.layer2 import Layer2
from boto.cloudsearch2.domain import Domain


#Hide the end point
doc_service = boto.cloudsearch2.document.DocumentServiceConnection(domain=None, endpoint='*')



class StdOutListener(StreamListener):
    def on_data(self, data):
        json_load = json.loads(data)
        dic = {}
        try:
            coordinates = json_load['coordinates']
            place = json_load['place']
            text = json_load['text']
            lang = json_load['lang']
            if lang == 'en':
                if coordinates != None:
                    dic['type'] = 'add'
                    dic['id'] = str(json_load['id'])
                    dic['fields'] = {'coordinates':[str(coordinates["coordinates"][0]),str(coordinates["coordinates"][1])],
                                    'text':text}
                    doc_service.add(dic['id'],  dic['fields'])
                    doc_service.commit()


                elif place != None:
                    #print i
                    dic['type'] = 'add'
                    dic['id'] = str(json_load['id'])
                    coord1 = (place["bounding_box"]["coordinates"][0][0][0] + place["bounding_box"]["coordinates"][0][2][0])/2
                    coord2 = (place["bounding_box"]["coordinates"][0][0][1] + place["bounding_box"]["coordinates"][0][2][1])/2
                    dic['fields'] = {'coordinates':[str(coord1),str(coord2)],
                                    'text':text}
                    append_record(dic)
                    doc_service.add(dic['id'],  dic['fields'])
                    doc_service.commit()

        except:
            pass
        return True
    
    def on_error(self, status):
        print(status)

def start_stream(auth, l):
    while True:
        try:
            stream = Stream(auth, l)
            stream.sample()
        except:
            continue


if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    start_stream(auth, l)
