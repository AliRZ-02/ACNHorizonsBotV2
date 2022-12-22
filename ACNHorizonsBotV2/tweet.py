from tweet_generator.extractor import Extractor
from tweet_generator.generate_tweets import tweet_with_verification
from tweet_generator.parse_tweets import parse_tweets
from tweet_generator.get_tweets import get_tweets
from utils.config.settings import Tweets

def tweet_helper(extractor: Extractor, tweet_type: Tweets) -> None:
    data = get_tweets(extractor, tweet_type)
    tweets = parse_tweets(data, extractor, tweet_type)
    tweet_with_verification(extractor, tweets)

def tweet() -> None:
    extractor = Extractor()

    for tweet_type in [Tweets.VILLAGERS, Tweets.NORTH_CREATURES, Tweets.SOUTH_CREATURES]:
        tweet_helper(extractor, tweet_type)

if __name__ == "__main__":
    tweet()