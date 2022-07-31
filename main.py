import requests
from time import sleep
channelid = input('Channel ID: ')
url = 'https://discord.com/api/v9/channels/' + channelid + '/messages'
token = input('Token: ')

def work(url, tkn):
    sleep(300)
    header = {
         'authorization': tkn
    }
    payload = {
       'content': '_work'
    }
    rqst = requests.post(url, headers=header, data=payload)
    work(url, tkn)
work(url, token)