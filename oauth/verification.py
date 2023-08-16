from requests_oauthlib import OAuth1Session
from dataclasses import dataclass

@dataclass
class Verify:
    def verification(self, oauth):
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)

        return (
            base_authorization_url,
            authorization_url
        )
    
class GetAccessTokens:
    def get_access_token(self, consumer_key,consumer_secret,resource_owner_key,resource_owner_secret,verifier):
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        return (
            access_token,
            access_token_secret
        )