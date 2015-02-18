import re
import tweepy

def twipy():
    AUTH = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
    API = tweepy.API(AUTH)
    timeline = API.user_timeline('RLangTip')[0]
    tweet = str(timeline.text)
    tweet = re.sub('(#.+)', '', tweet)
    tweet = re.sub('(http://.+)', '', tweet)
    tweet = re.sub(':', '.', tweet)
    print '@RLangTip: ' + tweet
    
if __name__ == "__main__": 
    twipy()
