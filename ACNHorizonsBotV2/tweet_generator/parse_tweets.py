from datetime import datetime
from typing import Any, Dict, List
from tweet_generator.extractor import Extractor
from utils.config.settings import Tweets
from utils.logger import tweet_logger

def parse_tweets(data: Dict[str, Any], extractor: Extractor, mode: Tweets = None) -> List[Dict[str, Any]]:
    tweet_logger.info(f"<parse_tweets: parse_tweets.py> Parsing daily tweets. Received Query Information - {data.get('queryInfo', {})}")

    tweets = data.get('data', [])

    if not tweets:
        return tweets

    if mode and mode != Tweets.VILLAGERS:
        hemisphere = "North" if mode == Tweets.NORTH_CREATURES else "South"

        tweets.insert(0,
            {
                'tweet': f'[THREAD] Important information on the state of critters in the {hemisphere}ern Hemisphere',
                'url': f'/images/months/{datetime.now().month}/{hemisphere}'
            }
        )
    
    return tweets