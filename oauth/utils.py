from requests_oauthlib import OAuth1Session
import configparser
from dataclasses import dataclass

@dataclass
class OAuth:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('E:\My Projects\TwitterBot\credentials\config.ini')

        self.consumer_key = self.config['twitter']['consumer_key']
        self.consumer_secret = self.config['twitter']['consumer_secret']

        self.request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"


    def Oauth(self, verifier):
        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret)

        try:
            fetch_response = oauth.fetch_request_token(self.request_token_url)
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")
        
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)

        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        # Make the request
        oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

        return (
            authorization_url,
            oauth
            )
    
myaoth = OAuth()
authorization_url, oauth = myaoth.Oauth()