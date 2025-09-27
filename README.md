# Dev Meme Bot
A personal project - scraping, resizing, posting: dev memes on autopilot

<img src="poster/resources/insta.gif" width="400">

dev-meme-bot is an instagram bot that reposts **developer/programming memes** found on several tech-related subreddits.

This project is built on top of:
- **RedditImageScraper** by [Clarity Coders](https://github.com/ClarityCoders/RedditImageScraper).
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
```
dev-memes-bot/
│── poster/                  # Handles Instagram posting
│   ├── driver.py             # Main script to select & upload memes
│   ├── PicManager.py         # Manages image resizing and tracking
│   └── resources/            # Support files (e.g., picList.txt, insta.png)
│
│── scraper/                 # Handles Reddit scraping
│   ├── SubDownload.py        # Scrapes memes from subreddits
│   ├── sub_list.csv          # List of subreddits to scrape
│   ├── images/               # Downloaded meme images
│   ├── ignore_images/        # Bad/duplicate images to skip
│   └── utils/                # Helper functions (e.g., token creation)
│
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
│── token.pickle              # Reddit API auth token (auto-generated)
│── venv/                     # Local virtual environment (should be gitignored)
```

---

## How to Run  

### 1. Clone the repository  
```bash
git clone https://github.com/athulya-anil/dev-meme-bot.git
cd dev-memes-bot
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the scraper to fetch memes
```bash
cd scraper
python3 SubDownload.py
```
This will pull memes from the subreddits listed in sub_list.csv and store them in scraper/images/.

### 5. Run the poster to upload memes
```bash
cd ../poster
python3 driver.py
```
This will:
- Pick 3 random memes from scraper/images/
- Resize them into Instagram-friendly squares
- Upload them to your Instagram account

**Note** - be sure to add your username and password in the driver.py file.


