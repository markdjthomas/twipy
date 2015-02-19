import re
import tweepy

def twipy():
    AUTH = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
    API = tweepy.API(AUTH)
    timeline = API.user_timeline('RLangTip')[0]
    tweet = str(timeline.text)
    tweet = re.sub('(#.+)', '', tweet)  # comment out if you want hashtags
    tweet = re.sub('(http://.+)', '', tweet)  # comment out if you want urls
    print '@RLangTip: ' + tweet
    
if __name__ == "__main__": 
    twipy()
