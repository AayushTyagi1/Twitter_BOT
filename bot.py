import tweepy
from tkinter import *
from tkinter.filedialog import askopenfilename
import time
import datetime

consumer_key =
consumer_secret =
access_token = 
access_token_secret =

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

user = api.me()
print(user.name)
print(user.location)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("Followed everyone that is following " + user.name)

master = Tk()
master.title("TWitter Bot")
master.configure(bg='skyblue')

label1 = Label( master, text="Search",bg='skyblue',font=("bold",10))
E1 = Entry(master, bd =10,bg='lightgrey',fg='black')

label2 = Label( master, text="Number of Tweets",bg='skyblue',font=("bold",10))
E2 = Entry(master, bd =10,bg='lightgrey',fg='black')

label3 = Label( master, text="What you want to Respond",bg='skyblue',font=("bold",10))
E3 = Entry(master, bd =10,bg='lightgrey',fg='black')

label4 = Label( master, text="Do you want to Reply?",bg='skyblue',font=("bold",10))
E4 = Listbox(master, bd =10,height=2,exportselection=0,bg='lightgrey',fg='black')
E4.insert(1, 'yes') 
E4.insert(2, 'no') 

label5 = Label( master, text="Do you want to Retweet?",bg='skyblue',font=("bold",10))
E5 = Listbox(master, bd =10,height=2,exportselection=0,bg='lightgrey',fg='black')
E5.insert(1, 'yes') 
E5.insert(2, 'no') 

label6 = Label( master, text="Do you want to add to Favorite?",bg='skyblue',font=("bold",10))
E6 = Listbox(master, bd =10,height=2,exportselection=0,bg='lightgrey',fg='black')
E6.insert(1, 'yes') 
E6.insert(2, 'no') 

label7 = Label( master, text="Do you want to follow Follow?",bg='skyblue',font=("bold",10))
E7 = Listbox(master, bd =10,height=2,exportselection=0,bg='lightgrey',fg='black')
E7.insert(1, 'yes') 
E7.insert(2, 'no') 

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()


def getE4():
    return str((E7.get(ACTIVE)))

def getE5():
    return str((E7.get(ACTIVE)))

def getE6():
    return str((E7.get(ACTIVE)))

def getE7():
    return str((E7.get(ACTIVE)))

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
    
def mainFunction():
    getE1()
    search = getE1()
    
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    
    getE3()
    phrase = getE3()
    
    getE4()
    reply = getE4()
    
    getE5()
    retweet = getE5()
    
    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break


    if retweet == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print('Retweeted the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed the user')
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break       
            
submit = Button(master, text ="Submit",fg='white',bg='dark blue', command = mainFunction)
Update = Button(master, text ="Update Daily Tweet",fg='black',bg='cyan', command = publictweet)

Update.pack()
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side =BOTTOM)

master.mainloop()
