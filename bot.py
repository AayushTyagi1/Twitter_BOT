import tweepy
from tkinter import *
from tkinter.filedialog import askopenfilename

consumer_key = "mcw0fusJiO6oCWIgXNOqfZm4f"
consumer_secret = "vlCJO6YKa5Bpnh1bMNc8JbRkUYs31cCEKAPvLVD6iTTauM0qVj"
access_token = '1258010808656842758-I5kRigF1FkpMXx7GqeLH8HXEcVsSoP'
access_token_secret = '905GceOgjqGIzZSsx6QcmPo8I3h3SSiUCp8NgS8gnlinM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth,wait_on_rate_limit=True)
'''
user = api.me()
print(user.name)
print(user.location)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("Followed everyone that is following " + user.name)
'''
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
                sleep(5)

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