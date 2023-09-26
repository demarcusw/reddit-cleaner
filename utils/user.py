import praw
import os
import logging
import lorem
import random

from . import logger
from .constants import *


class MyUser:
    def __init__(self) -> None:
        self.id = os.environ.get("BOTID")
        self._secret = os.environ.get("BOTSECRET")
        self._password = os.environ.get("PASSWORD")
        self.username = f"{AUTHOR}"
        self.logger = logger.MyLogger("CleanerLogger")

        if self.id and self._secret and self._password:
            pass
        else:
            self.logger.log(
                f"Missing env var!\nBOTID: {self.id}\nBOTSECRET: {self._secret}\nPASSWORD: {self._password}",
                level=logging.CRITICAL,
            )
            exit(-1)

        self._reddit = praw.Reddit(
            client_id=self.id,
            client_secret=self._secret,
            password=self._password,
            user_agent=USER_AGENT,
            username=self.username,
        )
        self.me = self._reddit.redditor(self.username)

    def _generate_junk(self) -> str:
        """
        Generates junk Lorem ipsum output of variable length/structure.
        Useful for overwriting comments before deletion.

        :return: Lorem Ipsum string of variable length/structure
        """
        sentence_count = random.randint(1, 7)
        comma_count = random.randint(0, 5)
        word_rang = random.randint(4, 11)

        return lorem.get_sentence(
            count=sentence_count, comma=comma_count, word_range=word_rang, sep=" "
        )

    def clean(self) -> None:
        """
        Iterates through all user submissions and comments
        and deletes them. Optionally, overwrite comment
        before deletion

        :return: None
        """
        # Clean all submitted posts
        for submission in self.me.submissions.new():
            self.logger.log(f"Deleting post: {submission.title}")
            submission.delete()

        # Clean all comments
        counter = 0
        comments = 0
        while counter < 10:
            for comment in self.me.comments.new(limit=None):
                post_title = comment.submission.title
                subrdt = comment.subreddit.display_name
                self.logger.log(f"Deleting comment on post: {post_title} in r/{subrdt}")
                new_body = self._generate_junk()
                comment.edit(new_body)
                comment.delete()
                comments += 1
            counter += 1

        self.logger.log(f"Deleted {comments} comments", level=logging.INFO)
