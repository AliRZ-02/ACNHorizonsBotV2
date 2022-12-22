import io
from datetime import datetime
from typing import Any, Dict, List
from tweet_generator.extractor import Extractor
from utils.logger import tweet_logger
from utils.config.settings import TWITTER_API_SECRET, TWITTER_API_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, API_URL
import tweepy

def tweet_with_verification(extractor: Extractor, tweets: List[Dict[str, Any]]) -> None:
    try:
        generate_tweets(extractor, tweets)
        tweet_logger.info(f'<tweet_verification: generate_tweets.py> Tweet Authenticated. The tweets for {datetime.now()} have been successfully sent')
    except Exception as e:
        tweet_logger.error(f'<tweet_verification: generate_tweets.py> Ran into an error with tweets for {datetime.now()}. Received error: {e}')
        raise Exception()

def generate_tweets(extractor: Extractor, tweets: List[Dict[str, Any]]) -> int:
    """Returns status code"""
    api = authenticate()

    prev_id = None
    for idx, tweet_data in enumerate(tweets):
        tweet = tweet_data.get("tweet", None)
        image = tweet_data.get("url", None)

        if idx:
            tweet = f'@ACNHorizonsBot {tweet}'

        image_url = f'{API_URL}{image}' if image is not None else None
        prev_id = tweet_fn(extractor, api, prev_id, tweet, image_url)

def authenticate() -> tweepy.API:
    auth = tweepy.OAuth1UserHandler(
        consumer_key=TWITTER_API_KEY, 
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_SECRET
    )

    return tweepy.API(auth)

def tweet_fn(extractor: Extractor, api: tweepy.API, prev_id: int, tweet: str, image_url: str) -> int:
    images = []
    if image_url:
        image = extractor.get_images(image_url).content
        image_upload = api.media_upload(filename='image.jpg', file=io.BytesIO(image))
        images.append(image_upload.media_id)

    if tweet:
        return api.update_status(status=tweet, media_ids=images, in_reply_to_status_id=prev_id).id
    
    return prev_id