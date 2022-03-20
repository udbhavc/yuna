import tweets
import utils
import tweepy
import theme
import markovify
from datetime import date, datetime
import time
from random import choice

from PyDictionary import PyDictionary
dictionary = PyDictionary()


def generate_tweet_text(themes):
    theme=themes
    filename = ("corpus/{}.txt").format(theme)
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    text = utils.strip_non_ascii(text)

    text_model = markovify.Text(text)

    sentence = text_model.make_short_sentence(225)  # generate short tweet

    return sentence


def main():
    # set initial date and emotion
    emotion = "love"
    olddate = date(2022, 3, 20)
    while(True):
        # check if new date
        if date.today() > olddate:
            olddate = date.today()
            emotion = theme.randomtheme()
        else:
            tweets.update_description(
                "Makima simp")
        text = generate_tweet_text(emotion)
        tweets.post_tweet(text)
        time.sleep(43200)  # wait half an hour before next tweet

if __name__ == "__main__":
    main()