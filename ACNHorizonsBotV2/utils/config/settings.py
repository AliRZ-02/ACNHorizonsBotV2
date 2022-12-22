import os
from typing import Optional
from enum import Enum

### Enums
class Tweets(Enum):
    VILLAGERS = 0
    NORTH_CREATURES = 1
    SOUTH_CREATURES = 2
    ALL = 3

### Environment Variables
SECRETS_FOLDER_PATH = os.getenv('SECRETS_FOLDER_PATH', None)
API_URL = os.getenv(f"API_URL", "https://acnhapiv2.onrender.com")

### Constants
ENDPOINTS = [f"{API_URL}/tweets/today/villagers", f"{API_URL}/tweets/today/North", f"{API_URL}/tweets/today/South", f"{API_URL}/tweets/today"]

### Secrets
def read_secrets(secret_name: str) -> Optional[None]:
    try:
        with open(f"{SECRETS_FOLDER_PATH}/{secret_name}") as f:
            return f.read()
    except IOError:
        return os.getenv(secret_name, None)

TWITTER_API_KEY = read_secrets("TWITTER_API_KEY")
TWITTER_API_SECRET = read_secrets("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = read_secrets("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = read_secrets("TWITTER_ACCESS_SECRET")