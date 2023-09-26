#!usr/bin/env python3
"""

1) Grab submissions from my user sorted by new
2) Call submission.delete
3) Grab all comments from my user, sorted by new
4) Call comment.delete
5) Done

"""
import argparse
from utils.user import MyUser


def main():
    parser = argparse.ArgumentParser(description="Reddit History Cleaner")

    # Define the arguments
    parser.add_argument(
        "--location",
        "-w",
        metavar="<log_location>",
        help="Full path to log location (default is STDOUT)",
    )

    parser.add_argument(
        "--overwrite",
        "-o",
        action="store_true",
        help="Overwrite comments with junk before deleting",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Access the argument values
    log_location = args.location
    overwrite = args.overwrite

    # Perform actions based on the arguments
    if log_location:
        print(f"Log location specified: {log_location}")
    else:
        print("No log location specified. Using STDOUT.")

    if overwrite:
        print(
            "Overwrite option enabled. Comments will be overwritten with junk before deleting."
        )

    me = MyUser(overwrite, log_location)
    me.clean()


main()
