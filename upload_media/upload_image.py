from dataclasses import dataclass

@dataclass
class UploadMedia:
    def upload_image(self, image, oauth):
        media_upload_url = "https://upload.twitter.com/1.1/media/upload.json"
        
        media_params = {
            'media':image
        }

        media_response = oauth.post(media_upload_url, files=media_params)
        media_id = media_response.json()['media_id_string']

        tweet_params = {
            "text": "currently laughing at my life. lmaoo",
            "media": {"media_ids": ["{}".format(media_id)]}
            }
        
        return(
            media_id,
            tweet_params
        )
