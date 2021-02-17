import praw
import datetime
import smtplib
from psaw import PushshiftAPI



personal_use_script = "LIOAUck3ax7u0A"
secret_name = "TUrtEoi0nEv2StITWipuuCFGo9C-XA"

reddit = praw.Reddit(client_id=personal_use_script,
                     client_secret=secret_name,
                     user_agent='ScrapeyBoi',
                     username='Warm_Welder_7716',
                     password='password')

api = PushshiftAPI(reddit)
subreddit = reddit.subreddit('pennystocks')

new_subreddit = subreddit.new()

time_text = {}
def get_date(created):
    return datetime.datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')
"""
for i in new_subreddit:
    created = get_date(i.created)
    title = str(i.title)
    text = str(i.selftext)
    time_text[created] = [title + text,i.score]

for i in time_text:
    print(str(i) + "      " + str(time_text[i][1]))
"""
#start_epoch=int(datetime.datetime(2021, 2, 1).timestamp())
#end_epoch=int(datetime.datetime(2021, 2, 8).timestamp())
#result = list(api.search_submissions(after=start_epoch,before=end_epoch,subreddit='pennystocks',filter=['url','author', 'title', 'subreddit']))

#print(len(result))
#for i in result:
    #print(i.title)
    #print()

