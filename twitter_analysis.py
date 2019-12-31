import twitter
from keys import TWITTER_OAUTH_SECRET, TWITTER_OAUTH_TOKEN, TWITTER_CONSUMER_SECRET, TWITTER_CONSUMER_KEY

# initialize api instance
twitter_api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                          consumer_secret=TWITTER_CONSUMER_SECRET,
                          access_token_key=TWITTER_OAUTH_TOKEN,
                          access_token_secret=TWITTER_OAUTH_SECRET)

# test authentication
print(twitter_api.VerifyCredentials())


