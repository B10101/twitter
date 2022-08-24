import pandas as pd
import snscrape.modules.twitter as twit
from time import sleep


usernames = ['Quincy Larson' , 'freeCodeCamp.org', 'Jeff Delaney', 'Moshfegh Hamedani', 'Fireship']


def get_tweets(username):
    tweet_data = list()

    number = 20

    for i, tweets in enumerate(twit.TwitterSearchScraper('{}'.format(username)).get_items()):
        if i>number:
            break
        tweet_data.append([tweets.date, tweets.content, tweets.user.username, tweets.url])

    df = pd.DataFrame(tweet_data, columns = ['Date', 'Tweets', 'Username', 'Url'])
    df.to_csv(f'{username}.csv', index=False,encoding='utf-8')
   


if __name__ =="__main__":
    for i in usernames:
        get_tweets(i)