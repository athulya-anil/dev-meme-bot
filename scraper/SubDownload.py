import praw
import requests
import cv2
import numpy as np
import os
import pickle

from utils.create_token import create_token

POST_SEARCH_AMOUNT = 30

# Create directory if it doesn't exist to save images
def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    if not CHECK_FOLDER:
        os.makedirs(image_path)

# Paths
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "images/")
ignore_path = os.path.join(dir_path, "ignore_images/")
create_folder(image_path)

# Get token file to log into reddit
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
else:
    creds = create_token()
    with open("token.pickle", "wb") as pickle_out:
        pickle.dump(creds, pickle_out)

reddit = praw.Reddit(
    client_id=creds['client_id'],
    client_secret=creds['client_secret'],
    user_agent=creds['user_agent'],
    username=creds['username'],
    password=creds['password']
)

f_final = open("sub_list.csv", "r")

for line in f_final:
    sub = line.strip()
    subreddit = reddit.subreddit(sub)

    print(f"Starting {sub}!")
    count = 0

    for submission in subreddit.hot(limit=POST_SEARCH_AMOUNT):
        if submission.over_18:
            continue  # skip NSFW

        if "jpg" in submission.url.lower() or "png" in submission.url.lower():
            try:
                # Download image
                resp = requests.get(submission.url.lower(), stream=True).raw
                image = np.asarray(bytearray(resp.read()), dtype="uint8")
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)

                if image is None:
                    print(f"Failed to decode image from {submission.url}")
                    continue

                # Resize for comparison
                compare_image = cv2.resize(image, (224, 224))

                # Collect ignore images
                ignore_paths = []
                for (dirpath, dirnames, filenames) in os.walk(ignore_path):
                    ignore_paths.extend([os.path.join(dirpath, file) for file in filenames])

                ignore_flag = False
                for ignore_file in ignore_paths:
                    ignore_img = cv2.imread(ignore_file)
                    if ignore_img is None:
                        continue

                    try:
                        difference = cv2.subtract(ignore_img, compare_image)
                        b, g, r = cv2.split(difference)
                        total_difference = (
                            cv2.countNonZero(b) +
                            cv2.countNonZero(g) +
                            cv2.countNonZero(r)
                        )
                        if total_difference == 0:
                            ignore_flag = True
                            break
                    except Exception as e:
                        print(f"Error comparing with ignore image {ignore_file}: {e}")
                        continue

                # Save image if not ignored
                if not ignore_flag:
                    out_file = f"{image_path}{sub}-{submission.id}.JPG"
                    cv2.imwrite(out_file, image)
                    count += 1

            except Exception as e:
                print(f"Image failed. {submission.url.lower()}")
                print(e)
