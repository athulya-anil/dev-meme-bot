import os
import random
from instagrapi import Client
from PIL import Image

# Directory where scraped images are stored
images_dir = os.path.join("..", "scraper", "images")

# Pick 3 random images
all_images = [f for f in os.listdir(images_dir) if f.lower().endswith(".jpg")]
pics = random.sample(all_images, 3)

# Full paths
album_path = [os.path.join(images_dir, p) for p in pics]

# Resize before posting
for p in album_path:
    try:
        im = Image.open(p)
        im.thumbnail((1080, 1080))
        im.save(p)  # overwrite resized image
        print(f"Resized: {p}")
    except Exception as e:
        print(f"Failed to resize {p}: {e}")

# Instagram login
bot = Client()
bot.login("dev.memes25", "H3HbShgH3HbShg")

# Caption for the post
text = "#funnycoder #internmemes #nerdy #codinghumor #vibecoding #100daysofcode #devlife #redditmemes #swe #vibecoder"

print("Uploading:", album_path)
bot.album_upload(album_path, caption=text)
