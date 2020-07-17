import tweepy
print("This is my Twitter bot")
consumer_key = "mcw0fusJiO6oCWIgXNOqfZm4f"
consumer_secret = "vlCJO6YKa5Bpnh1bMNc8JbRkUYs31cCEKAPvLVD6iTTauM0qVj"

Access_key = "1258010808656842758-7BEaWROlznbDVkcEER8A1NEXXo1sPB"
Access_secret = "8ENieweiFNfsHjK1PdWXPoQoposm08M7MJ50GIbyReFBj"

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
    if "#helloworld" in mention.text.lower():
        print("Find HelloWord")
        print("Responding back ..")
