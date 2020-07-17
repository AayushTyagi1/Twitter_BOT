import tweepy
import time
import datetime

print("This is my Twitter bot")
consumer_key = 
consumer_secret =

Access_key =
Access_secret =

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Access_key, Access_secret)

api=tweepy.API(auth)

mentions=api.mentions_timeline()
'''
print(mentions[0].__dict__.keys())
print(mentions[0].text)
print(mentions[0].id) '''

for mention in mentions:
    print(str(mention.id) +" - " + mention.text)
    if "#helloworld" in mention.text.lower():
        print("Find HelloWord")
        print("Responding back ..")
        api.update_status('@'+mention.user.screen_name+ "Hey back to you!",mention.id)
      
def publictweet():
    if datetime.date.today().weekday() == 0:
        tweettopublish = 'Hi everyone, today is Monday.   #Monday '
    if datetime.date.today().weekday() == 1:
        tweettopublish = 'Enjoy your Tuesday.  #Tuesday'
    if datetime.date.today().weekday() == 2:
        tweettopublish = 'Third week of the Week. #Wednesday'
    if datetime.date.today().weekday() == 3:
        tweettopublish = 'Thursday. I cannot wait for the Weekend'
    if datetime.date.today().weekday() == 4:
        tweettopublish = 'Friday...Finally'
    if datetime.date.today().weekday() == 5:
        tweettopublish = 'Great it is Saturday #weekend #Saturday'
    if datetime.date.today().weekday() == 6:
        tweettopublish = 'Sunday morning...#Weekend #enjoy '
    api.update_status(tweettopublish)
    print(tweettopublish)
publictweet()
