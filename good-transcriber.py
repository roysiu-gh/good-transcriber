#!/usr/bin/env python3
import praw, pdb, re, os

PRAW_BOT_SITE = "good-transcriber"
REPLIED_FILE = "replied.txt"
COMMENT_SEARCH = "I am a bot and I thank these amazing humans who are transcribing for the community"
COMMENT_REPLY = """good ~~bot~~ ~~human~~ bot

---

^(I am a bot, my initial mission was to thank the transcribers of reddit until I discovered that u/you_are_good_human existed, so I guess I'm doing this instead)"""

reddit = praw.Reddit(PRAW_BOT_SITE)
subreddit = reddit.subreddit("pythonforengineers")

current_replied = []

#if os.path.isfile(REPLIED_FILE):
with open(REPLIED_FILE, "r+") as f:
    mid = f.read().split("\n")  # Split entries in REPLIED_FILE into a list
    old_replied = [i for i in mid if i]  # Remove empty entries

for comment in subreddit.stream.comments():
    if re.search(COMMENT_SEARCH, comment.body, re.IGNORECASE):
        comment.reply(COMMENT_REPLY)
        print("Author: ", comment.author)
        print("Body: ", comment.body)
        print("Score: ", comment.score)

print(current_replied)

with open(REPLIED_FILE, "a+") as f:
    for post_id in current_replied:
        f.write(post_id + "\n")