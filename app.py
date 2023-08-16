from requests_oauthlib import OAuth1Session
import json
import requests
import time

from oauth.authenticate import Authenticate
from oauth.verification import Verify, GetAccessTokens
from upload_media.upload_image import UploadMedia
from media_links.fetch_image import GetItems

import configparser

config = configparser.ConfigParser()
config.read('credentials/config.ini')

consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

authentication = Authenticate()
resource_owner_key, resource_owner_secret = authentication.initiate_authentication(request_token_url,oauth)

print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
verify = Verify()
base_authorization_url, authorization_url = verify.verification(oauth)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

get_token = GetAccessTokens()
access_token, access_token_secret =  get_token.get_access_token(consumer_key, consumer_secret, resource_owner_key, resource_owner_secret, verifier)

print("Got Access token: %s" % access_token)
print("Got Access token Secret: %s" % access_token_secret)

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

images = GetItems()
image_urls = images.get_image() 

count = 1

for img in image_urls:
    image = requests.get(img).content

    uploads = UploadMedia()
    media_id, tweet_params = uploads.upload_image(image, oauth)
    print(f"Got the media ID: {media_id}")

    tweet_params = {
        "text": f"Day {count}! Lmaoo",
        "media": {"media_ids": ["{}".format(media_id)]}
        }

    count+=1

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=tweet_params,
    )


    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

    print(f'Tweet successful!')

    time.sleep(20)
