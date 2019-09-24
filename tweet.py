"""Assignment 1.
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False
    """

    return len(text) >= 1 and len(text) <= MAX_TWEET_LENGTH


def compare_tweet_lengths(first_tweet, second_tweet) -> int:
    """ Return 1 if first_tweet is longer than second_tweet,
    return -1 if second_tweet is longer than first_tweet,
    return 0 if first_tweet and second_tweet are the same length.

    Precondition: first_tweet and second_tweet are vaild tweets.

    >>> compare_tweet_lengths("Standing ovation", "Congratulations")
    1
    >>> compare_tweet_lengths("Congrats", "Hello Me")
    0
    """

    if(len(first_tweet) > len(second_tweet)):
        return 1
    elif(len(first_tweet) < len(second_tweet)):
        return -1
    else:
        return 0



def add_hashtag(tweet: str, tweet_word: str) -> str:
    """

    """
    if(MAX_TWEET_LENGTH>14):
        return tweet + " " + HASHTAG_SYMBOL + tweet_word
    else:
        return tweet


def contains_hashtag(tweet: str, tag: str) -> bool:
    """
    """

    pass


def is_mentioned(tweet: str, mentioned: str) -> bool:
    """
    """
    pass


def add_mention_exclusive(tweet: str, mention: str) -> str:
    """
    """
    pass


def num_tweets_required(tweet: str) -> int:
    """
    """
    pass


def get_nth_tweet(tweet: str, tweet_num: int) -> str:
    """
    """
    pass


# A helper function.  Do not modify this function, but you are welcome
# to call it.

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str


tweet = input("tweet: \n")
print(is_valid_tweet(tweet))