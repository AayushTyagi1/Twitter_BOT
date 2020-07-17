import tweepy
print("This is my Twitter bot")
consumer_key = ""
consumer_secret = ""

Access_key = ""
Access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Access_key, Access_secret)

api=tweepy.API(auth)

mentions=api.mentions_timeline()
''''
print(mentions[0].__dict__.keys())
print(mentions[0].text)
print(mentions[0].id) '''
for mention in mentions:
    print(str(mention.id) +" - " + mention.text)
