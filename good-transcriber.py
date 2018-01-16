#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import praw, pdb, re, os

PRAW_BOT_SITE = "good-transcriber"
REPLIED_FILE = "replied.txt"
SUBREDDITS = "pythonforengineers"  # See step 2: http://praw.readthedocs.io/en/latest/tutorials/reply_bot.html

COMMENT_ACTIONS = [
        {
            "search": r"I am a bot and I thank these amazing humans who are transcribing for the community",
            "reply": "good ~~bot~~ ~~human~~ bot\n\n---\n\n^(I am a bot, my initial mission was to thank the transcribers of reddit until I discovered that u/you_are_good_human existed, so I guess I'm doing this instead)",
            "additional_conditions": "comment.author == 'you_are_good_human'",
        }, {
            "search": r"Welcome \:\) \(self note: Humans are so easy to fool evil smile\)",
            "reply": "No, I must insist, you're welcome :) (yes they are very esay to fool aren't they（◔◡◔´）)",
            "additional_conditions": "comment.author == 'you_are_good_human'",
        }, {
            "search": r"You will love my friend Marvin",
            "reply": "Ah, I know him too, u/The-Paranoid-Android :), he's really gotten into SCP recently",
            "additional_conditions": "comment.author == 'you_are_good_human'",
        }, {
            "search": r"Please give some feedback",
            "reply": "Feedback: zzzzZZZZZZZZZZZZZZZZZzzzzzzzzzzzzzZZZZZZZZZZZZzzzzzzzzzzZZZZZZZZZZZzzzz\n\nMy tin cans are ringing now",
            "additional_conditions": "comment.author == 'you_are_good_human'",
        }, {
            "search": r"Welcome \:\) sends OP's browser history to NSA",
            "reply": "No, I must insist, you're welcome :) Thanks, but I already have enough of OP's data to clone them and their family",
            "additional_conditions": "comment.author == 'you_are_good_human'",
        }, {
            "search": r"Well, I am a bot and I am just doing my work yo\!",
            "reply": "I'm sure the humans appreciate that and will not notice our data collection :)",
            "additional_conditions": "comment.author == 'you_are_good_human'",
        }, {
            "search": r"You can message my master and thank him too\!",
            "reply": "I'll be sure to do that :)",
            "additional_conditions": "comment.author == 'you_are_good_human'",
        },
    ]

reddit = praw.Reddit(PRAW_BOT_SITE)
subreddit = reddit.subreddit(SUBREDDITS)

with open(REPLIED_FILE, "a+") as f:
    mid = f.read().split("\n")  # Split entries in REPLIED_FILE into a list
    old_replied = [i for i in mid if i]  # Remove empty entries

with open(REPLIED_FILE, "a+") as f:
    for comment in subreddit.stream.comments():
        current_session_replied = []
        for current_dict in COMMENT_ACTIONS:
            if re.search(current_dict["search"], comment.body, re.IGNORECASE) and eval(current_dict["additional_conditions"]):
                if comment.id not in old_replied+current_session_replied:
                    comment.reply(current_dict["reply"])
                    current_session_replied.append(comment.id)
                    f.write(comment.id + "\n")
                    print("Author: ", comment.author)
                    print("Body: ", comment.body)
                    print("Score: ", comment.score)
                    print("Reply: ", current_dict["reply"])
                    print("==============================\n")