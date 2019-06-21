import tweepy
import os
import time

print("Hello, I'm John Omnis and welcome to the future.")

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, "w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print("retrieving and replying to tweet")
    # REMEMBER TO USE 1118970173644369920 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,
                                     tweet_mode="extended")
    for mention in reversed(mentions):
        print(str(mention.id) + "_" + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if "#omnis" in mention.full_text.lower():
            print("found #omnis!")
            print("responding back...")
            api.update_status("@" + mention.user.screen_name + " Hi! I'm John#Omnis, welcome to the future", mention.id)


while True:
    reply_to_tweets()
    time.sleep(5)
