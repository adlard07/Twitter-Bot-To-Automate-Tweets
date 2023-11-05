# Twitter Bot

Welcome to the Twitter Bot project! This project allows you to easily automate post tweets through a Python script using the Twitter API and user tokens. You have the flexibility to customize and extend the bot's functionality using your own classes and functions. It utilizes web scraping with ChromeDriver to fetch memes from the web, and it also runs an image recognition bot to generate random and funny captions for the memes. The app is a lighthearted way to inject humor into your timeline whenever you need a study break or a laugh. 


## Features

Web Scraping: Twitter MemeBot uses ChromeDriver to search the web for coding memes, ensuring a fresh supply of humorous content.
Image Recognition: It employs an image recognition bot to identify objects, text, or patterns within the meme images.
Random Captions: After the image recognition process, the bot generates completely random and funny captions for each meme, ensuring that no caption is repeated.


## How It Works

The app uses ChromeDriver to browse the web and find coding memes. It fetches the meme images from various sources.
The image recognition bot analyzes each meme image to identify elements within the image.
Based on the image's content, the bot generates a humorous and random caption.
The app posts the meme with its caption to your Twitter account.

To get started, follow the instructions below.


## Prerequisites

Before using this Twitter bot, you need to have the following:

1. Python (>= 3.9)
2. Twitter Developer Account with a registered application
3. User tokens (Access Token and Access Token Secret) from your Twitter Developer Account

**Note:** Keep your Twitter API credentials confidential and avoid sharing them in public repositories.


## Run code

You can compile the code my using the command 
```bash
python -m app
```
This command will compile app.py by using the administrator rights. The administrator rights are neccessory because there are a few permissions that need to be granted before the compilation of the code. 


## Customization

You can extend the functionality of the Twitter bot by modifying the existing classes and functions or adding your own. For example, you could implement functions to retweet, like, or reply to tweets based on certain criteria.


## Hosting

You can host this app on a server of your choice, such as AWS, Heroku, or any other hosting platform. Set up a cron job or a scheduled task to run the app at your desired intervals. Once set up, you can forget about it for a few weeks, and Twitter MemeBot will continue to entertain your followers with coding memes.


## Contributing

If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request. Your contributions are greatly appreciated!

## Disclaimer

Please use this project responsibly and in compliance with Twitter's terms of service. Automated tweeting should be done ethically and not harm the Twitter community or violate any rules.

Thank you for choosing the Twitter Bot project! If you have any questions or need assistance, please don't hesitate to contact me at adelarddcunha@gmail.com. And make sure tu have fun ;)

Happy tweeting! 🐦🤖
