from utils.config.settings import ENDPOINTS, Tweets
import requests

class Extractor:
    """
    Extractor class mean to perform HTTP requests to collect tweetable info

    Fields:
        session: requests.Session
    
    Methods:
        get_tweets()
    """

    session: requests.Session

    def __init__(self) -> None:
        self.session = requests.Session()
    
    def get_tweets(self, tweets_type: Tweets = Tweets.ALL) -> requests.Response:
        return self.session.get(ENDPOINTS[tweets_type.value], timeout=None)
    
    def get_images(self, image_url: str) -> requests.Response:
        return self.session.get(image_url, timeout=None)
