# reddit-cleaner 🧹

Bot to auto clean Reddit history. Runs on a cronjob

## Description

I created this to automatically maintain good data hygeine w/r/t to my reddit account(s). Feel free to use it and customize it. I suggest running on a cronjob in the background.

## Usage

### STOP

🚨 IF YOU HAVE NOT SETUP REDDIT API ACCESS YET THEN DO NOT CONTINUE. THIS SCRIPT REQUIRES API KEY/SECRET PAIR TO WORK <https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki> 🚨

```bash
git clone git@github.com:demarcusw/reddit-cleaner.git
cd reddit-cleaner/
pip install -r requirements.txt
export BOTID=client_id
export BOTSECRET=client_secret
export PASSWORD=account_password
python clean.py --help
```

Reddit History Cleaner

**Options**

```
  -h, --help            show this help message and exit

  --location <log_location>, -w <log_location>
                        Full path to log location (default is STDOUT)

  --overwrite, -o       Overwrite comments with junk (Lorem Ipsum) before deleting
```
