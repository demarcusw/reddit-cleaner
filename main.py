#!usr/bin/env python3
"""

1) Grab submissions from my user sorted by new
2) Call submission.delete
3) Grab all comments from my user, sorted by new
4) Call comment.delete
5) Done

"""
from utils.user import *


me = MyUser()
me.clean()
