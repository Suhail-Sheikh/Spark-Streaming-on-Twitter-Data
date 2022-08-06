import tweepy
import os
import logging
import json
topic_name = "twitterdata"

search_input = "#ukraine,#fuck"
consumer_key = 'g8qhoRayrGJoKGrisuN6xNCHL'

consumer_secret = 'LWsqp9jBPy8rBc20WShYeLCAsz21DKIDb29tx7MTEN8MkeCsDu'

access_token = '1106363006-jsnIwQYqjwaaoCitn2ziK2Uv1ZRVGTQXngD6KCd'

access_secret = '7SXlXBPHzf9tqXh5wXoYhNR0XfHWvY4k4oHjK0WpZOrl2'
logger = logging.getLogger(__name__)


class TwitterStreamer():
    def stream_data(self):
        logger.info(f"{topic_name} Stream starting for {search_input}...")

        twitter_stream = MyListener(
            consumer_key, consumer_secret, access_token, access_secret)
        twitter_stream.filter(track=["#ipl"])
        twitter_stream.filter(track=["#ukraine"])


class MyListener(tweepy.Stream):
    def on_data(self, data):
        try:
            #producer.send(topic_name, data)
            msg = json.loads(data)
            print(msg)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


if __name__ == "__main__":
    TS = TwitterStreamer()
    TS.stream_data()
