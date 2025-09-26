# dev-memes-bot
A personal project - instagram bot! 

<img src="/poster/resources/insta.png" width="150">

dev-memes-bot is an instagram bot that reposts **developer/programming memes** found on several tech-related subreddits.

This project is built on top of:
- **RedditImageScraper** by [Clarity Coders](https://github.com/ClarityCoders/RedditImageScraper) (also check out their [YouTube](https://www.youtube.com/claritycoders)).
- **Instagrapi** [Instagrapi API](https://subzeroid.github.io/instagrapi/).

### How it works
1. The **scraper** (`scraper/SubDownload.py`) pulls fresh memes from your chosen subreddits and saves them to `/scraper/images`.
2. The **poster** (`poster/driver.py`) randomly selects 3 memes, resizes them to Instagram’s requirements, and uploads them as a carousel post.

### Features
- Automatically pulls memes from hand-picked developer humor subreddits.
- Avoids reposting the same meme twice (tracks already posted).
- The scraper is on safe mode and avoids 18+ or NSFW posts.
- Resizes images into perfect Instagram squares.
- Posts as a carousel with a consistent caption and hashtags.

## Folder Structure  

