# reddit-cleaner

Bot to auto clean Reddit history. Runs on a cronjob

## Arguments

`$ python clean.py --help`

Reddit History Cleaner

Options:

  -h, --help            show this help message and exit

  --location <log_location>, -w <log_location>
                        Full path to log location (default is STDOUT)

  --overwrite, -o       Overwrite comments with junk (Lorem Ipsum) before deleting

## Description

I created this to automatically maintain good data hygeine w/r/t to my reddit account(s). Feel free to use it and customize it. I suggest running on a cronjob in the background.
