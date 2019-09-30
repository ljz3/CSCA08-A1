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


def compare_tweet_lengths(first_tweet: str, second_tweet: str) -> int:
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
    return 0



def add_hashtag(tweet: str, tweet_word: str) -> str:
    """
    Return tweet concatinated with HASHTAG_SYMBOL and tweet_word
    if MAX_TWEET_LENGTH is at least 14.

    Preconditions: 
    tweet is a valid tweet.
    tweet_word is a valid tweet word.

    >>> add_hashtag('I like', 'cscA08')
    'I like #cscA08'
    >>> add_hashtag("You will need to paraphrase", "compsci")
    "You will need to paraphrase #compsci"
    """

    if(MAX_TWEET_LENGTH >= 14):
        return tweet + " " + HASHTAG_SYMBOL + tweet_word
    else:
        return tweet


def contains_hashtag(tweet: str, tag: str) -> bool:
    """
    Return True iff tweet contains a hashtag
    made up of HASHTAG_SYMBOL and the tag.
    Return False otherwise.

    Preconditions: 
    tweet is a valid tweet.
    tag is a valid tweet word.

    >>> contains_hashtag('I like #cscA08', 'cscA08')
    True
    >>> contains_hashtag('I like #cscA08', 'csc')
    False
    """

    return contains(tweet, tag, HASHTAG_SYMBOL)


def is_mentioned(tweet: str, mentioned: str) -> bool:
    """
    Return True iff tweet contains a mention
    made up of MENTION_SYMBOL and mentioned.
    Return False otherwise.

    Preconditions: 
    tweet is a valid tweet.
    mentioned is a valid tweet word.

    >>> is_mentioned('Go @Raptors!', 'Raptors')
    True
    >>> contains_hashtag('Good morning @Kevin', 'Kev')
    False
    """

    return contains(tweet, mentioned, MENTION_SYMBOL)



def add_mention_exclusive(tweet: str, mention: str) -> str:
    """
    Return tweet concatinated with a space, MENTION_SYMBOL and mention
    iff mention was not already mentioned in tweet.

    Preconditions: 
    tweet is a valid tweet.
    mention is a valid tweet word.

    >>> add_mention_exclusive("Go Raptors!", "Raptors)
    "Go Raptors! @Raptors"
    >>> add_mention_exclusive("Go @Raptors!")
    "Go @Raptors!"
    """

    if not is_mentioned(tweet, mention):
        return tweet + " " + MENTION_SYMBOL + mention
    else:
        return tweet


def num_tweets_required(tweet: str) -> int:
    """
    Return the minimum number of tweets that would be 
    required to communicate tweet.

    >>> num_tweets_required("I told my girlfriend she" 
    "drew her eyebrows too high. She seemed surprised.")
    2
    >>> num_tweets_required("Why is Peter Pan always flying? He neverlands.")
    1
    """

    return math.ceil(len(tweet)/MAX_TWEET_LENGTH)


def get_nth_tweet(tweet: str, tweet_num: int) -> str:
    """
    Return tweet split up into tweets of length MAX_TWEET_LENGTH
    at index tweet_num.

    >>> get_nth_tweet("I told my girlfriend she" 
    "drew her eyebrows too high. She seemed surprised.", 0)
    "I told my girlfriend shedrew her eyebrows too high"
    >>> get_nth_tweet("Woof woof!", 2)
    ""
    """

    return tweet[tweet_num * MAX_TWEET_LENGTH:(tweet_num+1) * MAX_TWEET_LENGTH]


# Helper Function
def contains(tweet: str, sub: str, symbol: str) -> str:
    """
    Return tweet concatinated with symbol and sub 
    if symbol is not already in sub.
    Return tweet concatinated with sub otherwise.

    >>> contains("Hello!", @Kevin, "@")
    "Hello! @Kevin"
    >>> contains("Good morning!", Kevin, "@")
    "Good morning! @Kevin"
    """
    
    if symbol in sub:
        return (sub + " ") in (clean(tweet) + " ")
    else:
        return (symbol + sub + " ") in (clean(tweet) + " ")
    

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