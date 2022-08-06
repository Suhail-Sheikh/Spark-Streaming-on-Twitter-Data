import tweepy
from tweepy import Stream
# from tweepy.Stream import StreamListener
from tweepy import OAuthHandler
import socket
import json

consumer_key = 'g8qhoRayrGJoKGrisuN6xNCHL'

consumer_secret = 'LWsqp9jBPy8rBc20WShYeLCAsz21DKIDb29tx7MTEN8MkeCsDu'

access_token = '1106363006-jsnIwQYqjwaaoCitn2ziK2Uv1ZRVGTQXngD6KCd'

access_secret = '7SXlXBPHzf9tqXh5wXoYhNR0XfHWvY4k4oHjK0WpZOrl2'

'''
api key - g8qhoRayrGJoKGrisuN6xNCHL
api key secret - LWsqp9jBPy8rBc20WShYeLCAsz21DKIDb29tx7MTEN8MkeCsDu
bearer token - AAAAAAAAAAAAAAAAAAAAAFOGbwEAAAAAgRqm90U5A%2Fex9JiP7bYIr8urnh8%3Ddyb4ACuJdz2hxN7lO0tnkFxADbEoTYz55HPZfGjji2Uc7l8WhQ



'''


class TweetsListener(Stream):

    # tweet object listens for the tweets

    def __init__(self, csocket):

        self.client_socket = csocket

    def on_data(self, data):

        try:

            msg = json.loads(data)

            print("new message")

            # if tweet is longer than 140 characters

            if "extended_tweet" in msg:

                # add at the end of each tweet "t_end"

                self.client_socket.send(
                    str(msg['extended_tweet']['full_text']+"t_end").encode('utf-8'))

                print(msg['extended_tweet']['full_text'])

            else:

                # add at the end of each tweet "t_end"

                self.client_socket.send(
                    str(msg['text']+"t_end").encode('utf-8'))

                print(msg['text'])

            return True

        except BaseException as e:

            print("Error on_data: %s" % str(e))

        return True

    def on_error(self, status):

        print(status)

        return True


def sendData(c_socket, keyword):

    print('start sending data from Twitter to socket')

    # authentication based on the credentials

    auth = OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_secret)

    # start sending data from the Streaming API

    twitter_stream = Stream(auth, TweetsListener(c_socket))

    twitter_stream.filter(track=keyword, languages=["en"])


if __name__ == "__main__":

    # server (local machine) creates listening socket

    s = socket.socket()

    host = "localhost"

    port = 8081

    s.bind((host, port))

    print('socket is ready')

    # server (local machine) listens for connections

    s.listen(4)

    print('socket is listening')

    # return the socket and the address on the other side of the connection (client side)

    c_socket, addr = s.accept()

    print("Received request from: " + str(addr))

    # select here the keyword for the tweet data

    sendData(c_socket, keyword=['piano'])

'''
Yes, we plan to perform sentimental analysis on the tweets based on hashtags used for a college mini-project. This data will not be published anywhere and will solely be used for college purposes.
'I will be using the API to perform sentiment analysis on a few tweets based on hashtags for a college mini project. This project will be using tweepy module in python to fetch the data from the API and perform streaming analysis as required by the college mini-project.''
'''
