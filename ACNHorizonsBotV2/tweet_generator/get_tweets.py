from typing import Any, Dict
from utils.config.settings import Tweets
from utils.logger import tweet_logger
from tweet_generator.extractor import Extractor

def get_tweets(extractor: Extractor, tweets_type: Tweets = Tweets.ALL) -> Dict[str, Any]:
    tweet_logger.info(f"<get_tweets: get_tweets.py> Collecting daily tweets")

    tweets = extractor.get_tweets(tweets_type)
    return tweets.json()
