import re
import tweepy
import HTMLParser

def twipy():
    AUTH = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
    API = tweepy.API(AUTH)
    timeline = API.user_timeline('RLangTip')[0]
    tweet = str(timeline.text)
    parser = HTMLParser.HTMLParser()
    print parser.unescape('@RLangTip: ' + tweet)
    
if __name__ == "__main__": 
    twipy()
