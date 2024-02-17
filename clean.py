#!usr/bin/env python3
"""
Algorithm:

1) Grab submissions from my user sorted by new
2) Call submission.delete
3) Grab all comments from my user, sorted by new
4) Call comment.delete
5) Done
"""
import praw
import os
import logging

VERSION = 0.1
APP_NAME = "Cleaner"
PLATFORM = "linux"


class MyLogger:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # create a stream handler for stdout
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        stream_handler.setFormatter(stream_formatter)
        self.logger.addHandler(stream_handler)

    def log(self, message, level=logging.DEBUG):
        # custom switch. based on logging level,
        # call corresponding logger function.
        # we store in dictionary for O(1) lookup
        log = {
            logging.DEBUG: self.logger.debug,
            logging.INFO: self.logger.info,
            logging.WARNING: self.logger.warning,
            logging.ERROR: self.logger.error,
            logging.CRITICAL: self.logger.critical
        }

        # call our specific logger level function
        log[level](message)


class MyUser:
    
    VERSION = 0.1
    APP_NAME = "Cleaner"
    PLATFORM = "linux"

    def __init__(self) -> None:
        self.id = os.environ.get('BI')
        self._secret = os.environ.get('BS')
        self._password = os.environ.get('P')
        self.username = os.environ.get('AUTHOR')
        self.logger = MyLogger('CleanerLogger')
        self.ua = f"{PLATFORM}:{APP_NAME}:v{VERSION} (by u/{self.username})"

        if self.id and self._secret and self._password:
            pass
        else:
            self.logger.log(
                f"Missing env var!\nBOTID: {self.id}\nBOTSECRET: {self._secret}\nPASSWORD: {self._password}", level=logging.CRITICAL)
            exit(-1)

        self._reddit = praw.Reddit(
            client_id=self.id,
            client_secret=self._secret,
            password=self._password,
            user_agent=self.ua,
            username=self.username,
        )
        self.me = self._reddit.redditor(self.username)

    def clean(self) -> None:
        # Clean all submitted posts
        for submission in self.me.submissions.new():
            self.logger.log(f"About to delete post: {submission.title}")
            submission.delete()

        # Clean all comments
        counter = 0
        comments = 0
        while counter < 10:
            for comment in self.me.comments.new(limit=None):
                post_title = comment.submission.title
                subrdt = comment.subreddit.display_name
                self.logger.log(
                    f"About to delete comment on post: {post_title} in r/{subrdt}")
                comment.delete()
                comments += 1
            counter += 1

        self.logger.log(f"Deleted {comments} comments", level=logging.INFO)

def main():
    me = MyUser()
    me.clean()

main()
