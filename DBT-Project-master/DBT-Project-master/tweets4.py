import pandas as pd
import tweepy
import random
import socket
# function to display data of each tweet


def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")


# function to perform data extraction
def scrape(words, numtweet):

    tweets = tweepy.Cursor(api.search_tweets,
                           words, lang="en",
                           tweet_mode='extended').items(random.randint(1, numtweet))
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        print(tweet)
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']


if __name__ == '__main__':

    # Enter your own credentials obtained
    # from your developer account
    consumer_key = 'g8qhoRayrGJoKGrisuN6xNCHL'

    consumer_secret = 'LWsqp9jBPy8rBc20WShYeLCAsz21DKIDb29tx7MTEN8MkeCsDu'

    access_key = '1106363006-jsnIwQYqjwaaoCitn2ziK2Uv1ZRVGTQXngD6KCd'

    access_secret = '7SXlXBPHzf9tqXh5wXoYhNR0XfHWvY4k4oHjK0WpZOrl2'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Enter Hashtag and initial date
    words = '#covid19'

    # number of tweets you want to extract in one run
    numtweet = 100
    scrape(words, numtweet)
    scrape("#ipl", numtweet)
    print('Scraping has completed!')
    s = socket.socket()

    host = "127.0.0.1"

    port = 8081

    s.bind((host, port))

    print('socket is ready')

    # server (local machine) listens for connections

    s.listen(4)

    print('socket is listening')

    # return the socket and the address on the other side of the connection (client side)

    c_socket, addr = s.accept()

    print("Received request from: " + str(addr))
