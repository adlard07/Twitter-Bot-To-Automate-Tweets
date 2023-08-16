from dataclasses import dataclass


@dataclass
class Authenticate:
    def initiate_authentication(self, request_token_url,oauth):
        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")

        return(
            resource_owner_key,
            resource_owner_secret
            )